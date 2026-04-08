import React, { useState, useEffect } from 'react';
import {
  Grid, Card, CardMedia, CardContent, Typography, CardActions, Button,
  Drawer, List, ListItem, ListItemText, IconButton, Badge, AppBar, Toolbar,
  Container, Dialog, DialogTitle, DialogContent, DialogActions, Alert, Snackbar
} from '@mui/material';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import DeleteIcon from '@mui/icons-material/Delete';
import api from '../Api';

export default function Shop() {
  const [products, setProducts] = useState([]);
  const [images, setImages] = useState({});
  const [cart, setCart] = useState([]);
  const [cartOpen, setCartOpen] = useState(false);
  const [orderSuccess, setOrderSuccess] = useState(null);

  // Загрузка товаров
  useEffect(() => {
    api.get('/products/').then(res => setProducts(res.data));
  }, []);

  // Загрузка изображений для товаров
  useEffect(() => {
    const fetchImages = async () => {
      const imgMap = {};
      for (let p of products) {
        try {
          const res = await api.get(`/images/product/${p.id}`);
          if (res.data && res.data.length > 0) imgMap[p.id] = res.data[0].image_url;
          else imgMap[p.id] = null;
        } catch { imgMap[p.id] = null; }
      }
      setImages(imgMap);
    };
    if (products.length) fetchImages();
  }, [products]);

  const addToCart = (product) => {
    setCart(prev => {
      const existing = prev.find(item => item.id === product.id);
      if (existing) return prev.map(item => item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item);
      return [...prev, { ...product, quantity: 1 }];
    });
  };

  const removeFromCart = (id) => {
    setCart(prev => prev.filter(item => item.id !== id));
  };

  const updateQuantity = (id, delta) => {
    setCart(prev => prev.map(item => {
      if (item.id === id) {
        const newQty = item.quantity + delta;
        if (newQty <= 0) return null;
        return { ...item, quantity: newQty };
      }
      return item;
    }).filter(Boolean));
  };

  const totalPrice = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  const placeOrder = async () => {
    try {
      const items = cart.map(item => ({ product_id: item.id, quantity: item.quantity }));
      const response = await api.post('/orders/', { items });
      setOrderSuccess({ message: `Заказ №${response.data.id} создан на сумму ${response.data.total_price} ₽` });
      setCart([]);
      setCartOpen(false);
    } catch (err) {
      setOrderSuccess({ error: err.response?.data?.detail || 'Ошибка оформления' });
    }
  };

  return (
    <div>
      <AppBar position="static" color="default" elevation={1}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>Товары</Typography>
          <IconButton color="inherit" onClick={() => setCartOpen(true)}>
            <Badge badgeContent={cart.length} color="secondary">
              <ShoppingCartIcon />
            </Badge>
          </IconButton>
        </Toolbar>
      </AppBar>
      <Container sx={{ mt: 4 }}>
        <Grid container spacing={3}>
          {products.map(product => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <Card>
                {images[product.id] && (
                  <CardMedia component="img" height="200" image={images[product.id]} alt={product.name} />
                )}
                <CardContent>
                  <Typography variant="h6">{product.name}</Typography>
                  <Typography variant="body2" color="text.secondary">{product.description}</Typography>
                  <Typography variant="h6" color="primary" sx={{ mt: 1 }}>{product.price} ₽</Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" variant="contained" onClick={() => addToCart(product)}>В корзину</Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>

      <Drawer anchor="right" open={cartOpen} onClose={() => setCartOpen(false)}>
        <List sx={{ width: 350, p: 2 }}>
          <Typography variant="h6" sx={{ mb: 2 }}>Корзина</Typography>
          {cart.length === 0 && <Typography>Корзина пуста</Typography>}
          {cart.map(item => (
            <ListItem key={item.id} secondaryAction={
              <IconButton edge="end" onClick={() => removeFromCart(item.id)}><DeleteIcon /></IconButton>
            }>
              <ListItemText
                primary={item.name}
                secondary={`${item.price} ₽ × ${item.quantity} = ${item.price * item.quantity} ₽`}
              />
              <Button size="small" onClick={() => updateQuantity(item.id, -1)}>-</Button>
              <span style={{ margin: '0 8px' }}>{item.quantity}</span>
              <Button size="small" onClick={() => updateQuantity(item.id, 1)}>+</Button>
            </ListItem>
          ))}
          {cart.length > 0 && (
            <>
              <Typography variant="h6" sx={{ mt: 2 }}>Итого: {totalPrice} ₽</Typography>
              <Button fullWidth variant="contained" sx={{ mt: 2 }} onClick={placeOrder}>Оформить заказ</Button>
            </>
          )}
        </List>
      </Drawer>

      <Snackbar open={!!orderSuccess} autoHideDuration={6000} onClose={() => setOrderSuccess(null)} anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}>
        <Alert severity={orderSuccess?.error ? 'error' : 'success'}>
          {orderSuccess?.error || orderSuccess?.message}
        </Alert>
      </Snackbar>
    </div>
  );
}