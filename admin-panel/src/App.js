// // import logo from './logo.svg';
// // import './App.css';

// // function App() {
// //   return (
// //     <div className="App">
// //       <header className="App-header">
// //         <img src={logo} className="App-logo" alt="logo" />
// //         <p>
// //           Edit <code>src/App.js</code> and save to reload.
// //         </p>
// //         <a
// //           className="App-link"
// //           href="https://reactjs.org"
// //           target="_blank"
// //           rel="noopener noreferrer"
// //         >
// //           Learn React
// //         </a>
// //       </header>
// //     </div>
// //   );
// // }

// // export default App;


// // import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
// // import { useState } from 'react';
// // import Login from './pages/Login';
// // import Products from './pages/Products';
// // import Categories from './pages/Categories';
// // import Brands from './pages/Brands';
// // import Images from './pages/Images';
// // import PrivateRoute from './components/PrivateRoute';
// // import Layout from './components/Layout';

// // function App() {
// //   const [isAuth, setIsAuth] = useState(!!localStorage.getItem('token'));

// //   return (
// //     <BrowserRouter>
// //       <Routes>
// //         <Route path="/login" element={<Login setAuth={setIsAuth} />} />
// //         <Route element={<PrivateRoute isAuth={isAuth} />}>
// //           <Route element={<Layout />}>
// //             <Route path="/products" element={<Products />} />
// //             <Route path="/categories" element={<Categories />} />
// //             <Route path="/brands" element={<Brands />} />
// //             <Route path="/images/:productId" element={<Images />} />
// //             <Route path="/" element={<Navigate to="/products" />} />
// //           </Route>
// //         </Route>
// //       </Routes>
// //     </BrowserRouter>
// //   );
// // }

// // export default App;


// import React, { useState, useEffect } from 'react';
// import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';
// import { ThemeProvider, createTheme } from '@mui/material/styles';
// import CssBaseline from '@mui/material/CssBaseline';
// import Container from '@mui/material/Container';
// import AppBar from '@mui/material/AppBar';
// import Toolbar from '@mui/material/Toolbar';
// import Typography from '@mui/material/Typography';
// import Button from '@mui/material/Button';
// import Box from '@mui/material/Box';
// import Login from './pages/Login';
// import Products from './pages/Products';
// import Categories from './pages/Categories';
// import Brands from './pages/Brands';
// import Images from './pages/Images';
// import Users from './pages/Users';
// import Shop from './pages/Shop';
// import Orders from './pages/Orders';
// import api from './Api';


// const theme = createTheme();

// function App() {
//   const [token, setToken] = useState(localStorage.getItem('access_token'));
//   const [user, setUser] = useState(null);

//   useEffect(() => {
//     if (token) {
//       api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
//       api.get('/auth/me')
//         .then(res => setUser(res.data))
//         .catch(() => logout());
//     } else {
//       delete api.defaults.headers.common['Authorization'];
//       setUser(null);
//     }
//   }, [token]);

//   const logout = () => {
//     localStorage.removeItem('access_token');
//     setToken(null);
//     setUser(null);
//   };

//   if (!token) {
//     return <Login onLogin={setToken} />;
//   }

//   const isAdmin = user?.role === 'admin';

//   return (
//     <ThemeProvider theme={theme}>
//       <CssBaseline />
//       <BrowserRouter>
//         <AppBar position="static">
//           <Toolbar>
//             <Typography variant="h6" sx={{ flexGrow: 1 }}>
//               Интернет-магазин
//             </Typography>
//             <Button color="inherit" component={Link} to="/shop">Магазин</Button>
//             <Button color="inherit" component={Link} to="/products">Товары</Button>
//             <Button color="inherit" component={Link} to="/categories">Категории</Button>
//             <Button color="inherit" component={Link} to="/brands">Бренды</Button>
//             <Button color="inherit" component={Link} to="/images">Изображения</Button>
//             <Button color="inherit" component={Link} to="/orders">Заказы</Button>
//             {isAdmin && (
//               <Button color="inherit" component={Link} to="/users">Пользователи</Button>
//             )}
//             <Button color="inherit" onClick={logout}>Выйти ({user?.username})</Button>
//           </Toolbar>
//         </AppBar>
//         <Container sx={{ mt: 4 }}>
//           <Routes>
//             <Route path="/shop" element={<Shop />} />
//             <Route path="/products" element={<Products />} />
//             <Route path="/categories" element={<Categories />} />
//             <Route path="/brands" element={<Brands />} />
//             <Route path="/images" element={<Images />} />
//             <Route path="/orders" element={<Orders />} />
            
//             {isAdmin && <Route path="/users" element={<Users />} />}
//             <Route path="/" element={<Navigate to="/shop" />} />
//           </Routes>
//         </Container>
//       </BrowserRouter>
//     </ThemeProvider>
//   );
// }

// export default App;

import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
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

  const logout = () => {
    localStorage.removeItem('access_token');
    setToken(null);
    setUser(null);
  };

  if (!token) {
    return <Login onLogin={setToken} />;
  }

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

            {/* Доступно всем авторизованным */}
            <Button color="inherit" component={Link} to="/shop">Магазин</Button>

            {/* Менеджер и админ */}
            {(isManager || isAdmin) && (
              <>
                <Button color="inherit" component={Link} to="/products">Товары</Button>
                <Button color="inherit" component={Link} to="/categories">Категории</Button>
                <Button color="inherit" component={Link} to="/brands">Бренды</Button>
                <Button color="inherit" component={Link} to="/images">Изображения</Button>
                <Button color="inherit" component={Link} to="/orders">Все заказы</Button>
              </>
            )}

            {/* Только для обычного пользователя */}
            {isUser && (
              <Button color="inherit" component={Link} to="/my-orders">Мои заказы</Button>
            )}

            {/* Только для админа */}
            {isAdmin && (
              <Button color="inherit" component={Link} to="/users">Пользователи</Button>
            )}

            <Button color="inherit" onClick={logout}>Выйти ({user?.username})</Button>
          </Toolbar>
        </AppBar>

        <Container sx={{ mt: 4 }}>
          <Routes>
            {/* Публичные маршруты для всех авторизованных */}
            <Route path="/shop" element={<Shop />} />
            <Route path="/my-orders" element={
              <ProtectedRoute allowedRoles={['user', 'manager', 'admin']} userRole={role}>
                <MyOrders />
              </ProtectedRoute>
            } />

            {/* Админские маршруты (только менеджер и админ) */}
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

            {/* Только для админа */}
            <Route path="/users" element={
              <ProtectedRoute allowedRoles={['admin']} userRole={role}>
                <Users />
              </ProtectedRoute>
            } />

            <Route path="/" element={<Navigate to="/shop" />} />
          </Routes>
        </Container>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;