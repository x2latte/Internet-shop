import React, { useState, useEffect } from 'react';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
  Paper, Button, Select, MenuItem, Typography, Box, CircularProgress
} from '@mui/material';
import api from '../Api';

const Orders = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchOrders = async () => {
    try {
      const res = await api.get('/orders/admin/all');
      setOrders(res.data);
    } catch (err) {
      console.error('Ошибка загрузки заказов:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleStatusChange = async (orderId, newStatus) => {
    try {
      await api.put(`/orders/${orderId}/status`, { status: newStatus });
      setOrders(prev =>
        prev.map(order =>
          order.id === orderId ? { ...order, status: newStatus } : order
        )
      );
    } catch (err) {
      console.error('Ошибка обновления статуса:', err);
    }
  };

  const handleDelete = async (orderId) => {
  if (window.confirm('Вы уверены, что хотите удалить заказ?')) {
    try {
      await api.delete(`/orders/${orderId}`);
      setOrders(prev => prev.filter(order => order.id !== orderId));
    } catch (err) {
      console.error('Ошибка удаления:', err);
    }
  }
};

  useEffect(() => {
    fetchOrders();
  }, []);

  if (loading) return <CircularProgress />;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Заказы</Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID заказа</TableCell>
              <TableCell>Пользователь (ID)</TableCell>
              <TableCell>Дата</TableCell>
              <TableCell>Сумма</TableCell>
              <TableCell>Статус</TableCell>
              {/* <TableCell>Действие</TableCell>  */}
              <TableCell>Удалить</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {orders.map(order => (
              <TableRow key={order.id}>
                <TableCell>{order.id}</TableCell>
                <TableCell>{order.user_id}</TableCell>
                <TableCell>{new Date(order.created_at).toLocaleString()}</TableCell>
                <TableCell>{order.total_price} ₽</TableCell>
                <TableCell>
                  <Select
                    value={order.status}
                    onChange={(e) => handleStatusChange(order.id, e.target.value)}
                    size="small"
                  >
                    <MenuItem value="pending">Ожидает оплаты</MenuItem>
                    <MenuItem value="paid">Оплачен</MenuItem>
                    <MenuItem value="shipped">Отправлен</MenuItem>
                    <MenuItem value="delivered">Доставлен</MenuItem>
                    <MenuItem value="cancelled">Отменён</MenuItem>
                  </Select>
                </TableCell>
                {/* <TableCell>
                  <Button variant="outlined" size="small">Детали</Button>
                </TableCell> */}
                <TableCell>
                <Button variant="contained" color="error" size="small" onClick={() => handleDelete(order.id)}>
                    Удалить
                </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Orders;