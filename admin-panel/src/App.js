import React, { useState, useEffect, useRef } from 'react';
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Snackbar, Alert } from '@mui/material';
import Login from './pages/Login';
import Products from './pages/Products';
import Categories from './pages/Categories';
import Brands from './pages/Brands';
import Images from './pages/Images';
import Users from './pages/Users';
import Shop from './pages/Shop';
import Orders from './pages/Orders';
import MyOrders from './pages/MyOrders';
import ProtectedRoute from './components/ProtectedRoute';
import api from './Api';

const theme = createTheme();

function App() {
  const [token, setToken] = useState(localStorage.getItem('access_token'));
  const [user, setUser] = useState(null);
  const [notification, setNotification] = useState(null);
  const ws = useRef(null);

  // Функция выхода (объявлена до эффектов)
  const logout = () => {
    localStorage.removeItem('access_token');
    setToken(null);
    setUser(null);
    if (ws.current) {
      ws.current.close();
    }
  };

  // Загрузка пользователя
  useEffect(() => {
    if (token) {
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      api.get('/auth/me')
        .then(res => setUser(res.data))
        .catch(() => logout());
    } else {
      delete api.defaults.headers.common['Authorization'];
      setUser(null);
    }
  }, [token]);

  // WebSocket-соединение для менеджеров/админов (безусловный хук)
  useEffect(() => {
    if (token && user && (user.role === 'manager' || user.role === 'admin')) {
      const wsUrl = `ws://localhost:8000/ws/manager?token=${token}`;
      ws.current = new WebSocket(wsUrl);

      ws.current.onopen = () => console.log('WebSocket подключён (менеджер/админ)');
      ws.current.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data.type === 'new_order') {
            setNotification(
              `Новый заказ №${data.order_id} от ${data.user} на сумму ${data.total} ₽`
            );
          }
        } catch (e) {
          console.error('Ошибка разбора сообщения WebSocket', e);
        }
      };
      ws.current.onclose = (event) => {
        console.log('WebSocket закрыт', event.reason);
      };
      ws.current.onerror = (error) => console.error('Ошибка WebSocket', error);

      return () => {
        ws.current.close();
      };
    }
  }, [token, user]);

  // Если нет токена — показываем страницу входа
  if (!token) {
    return <Login onLogin={setToken} />;
  }

  // Вычисление ролей
  const role = user?.role;
  const isAdmin = role === 'admin';
  const isManager = role === 'manager';
  const isUser = role === 'user';

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" sx={{ flexGrow: 1 }}>
              Интернет-магазин
            </Typography>

            <Button color="inherit" component={Link} to="/shop">Магазин</Button>

            {(isManager || isAdmin) && (
              <>
                <Button color="inherit" component={Link} to="/products">Товары</Button>
                <Button color="inherit" component={Link} to="/categories">Категории</Button>
                <Button color="inherit" component={Link} to="/brands">Бренды</Button>
                <Button color="inherit" component={Link} to="/images">Изображения</Button>
                <Button color="inherit" component={Link} to="/orders">Все заказы</Button>
              </>
            )}

            {isUser && (
              <Button color="inherit" component={Link} to="/my-orders">Мои заказы</Button>
            )}

            {isAdmin && (
              <Button color="inherit" component={Link} to="/users">Пользователи</Button>
            )}

            <Button color="inherit" onClick={logout}>Выйти ({user?.username})</Button>
          </Toolbar>
        </AppBar>

        <Container sx={{ mt: 4 }}>
          <Routes>
            <Route path="/shop" element={<Shop />} />
            <Route path="/my-orders" element={
              <ProtectedRoute allowedRoles={['user', 'manager', 'admin']} userRole={role}>
                <MyOrders />
              </ProtectedRoute>
            } />

            <Route path="/products" element={
              <ProtectedRoute allowedRoles={['manager', 'admin']} userRole={role}>
                <Products />
              </ProtectedRoute>
            } />
            <Route path="/categories" element={
              <ProtectedRoute allowedRoles={['manager', 'admin']} userRole={role}>
                <Categories />
              </ProtectedRoute>
            } />
            <Route path="/brands" element={
              <ProtectedRoute allowedRoles={['manager', 'admin']} userRole={role}>
                <Brands />
              </ProtectedRoute>
            } />
            <Route path="/images" element={
              <ProtectedRoute allowedRoles={['manager', 'admin']} userRole={role}>
                <Images />
              </ProtectedRoute>
            } />
            <Route path="/orders" element={
              <ProtectedRoute allowedRoles={['manager', 'admin']} userRole={role}>
                <Orders />
              </ProtectedRoute>
            } />

            <Route path="/users" element={
              <ProtectedRoute allowedRoles={['admin']} userRole={role}>
                <Users />
              </ProtectedRoute>
            } />

            <Route path="/" element={<Navigate to="/shop" />} />
          </Routes>
        </Container>
      </BrowserRouter>

      <Snackbar
        open={!!notification}
        autoHideDuration={6000}
        onClose={() => setNotification(null)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
      >
        <Alert onClose={() => setNotification(null)} severity="info" sx={{ width: '100%' }}>
          {notification}
        </Alert>
      </Snackbar>
    </ThemeProvider>
  );
}

export default App;