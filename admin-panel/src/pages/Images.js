// import React from 'react';

// const Images = () => {
//   return <div>Images Page (coming soon)</div>;
// };

// export default Images;

import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions, Alert, Snackbar, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import api from '../Api';

export default function Images() {
  const [images, setImages] = useState([]);
  const [products, setProducts] = useState([]);
  const [open, setOpen] = useState(false);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState({ image_url: '', product_id: '' });
  const [error, setError] = useState('');
  const [snack, setSnack] = useState(null);

  const fetchImages = async () => {
    const res = await api.get('/images/');
    setImages(res.data);
  };
  const fetchProducts = async () => {
    const res = await api.get('/products/');
    setProducts(res.data);
  };

  useEffect(() => {
    fetchImages();
    fetchProducts();
  }, []);

  const handleOpen = (item = null) => {
    if (item) { setEditing(item); setForm({ image_url: item.image_url, product_id: item.product_id }); }
    else { setEditing(null); setForm({ image_url: '', product_id: '' }); }
    setError('');
    setOpen(true);
  };

  const handleSave = async () => {
    try {
      if (editing) await api.put(`/images/${editing.id}`, form);
      else await api.post(`/images/?product_id=${form.product_id}`, { image_url: form.image_url });
      setSnack({ severity: 'success', text: editing ? 'Обновлено' : 'Добавлено' });
      fetchImages();
      setOpen(false);
    } catch (err) { setError(err.response?.data?.detail || 'Ошибка'); }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Удалить изображение?')) {
      await api.delete(`/images/${id}`);
      setSnack({ severity: 'info', text: 'Удалено' });
      fetchImages();
    }
  };

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'image_url', headerName: 'URL', width: 300 },
    { field: 'product_id', headerName: 'Товар ID', width: 120 },
    { field: 'actions', headerName: 'Действия', width: 200, renderCell: (params) => (<><Button size="small" onClick={() => handleOpen(params.row)}>Изменить</Button><Button size="small" color="error" onClick={() => handleDelete(params.row.id)}>Удалить</Button></>) }
  ];

  return (
    <div>
      <Button variant="contained" onClick={() => handleOpen()} sx={{ mb: 2 }}>Добавить изображение</Button>
      <DataGrid rows={images} columns={columns} autoHeight />
      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>{editing ? 'Изменить' : 'Новое изображение'}</DialogTitle>
        <DialogContent>
          {error && <Alert severity="error">{error}</Alert>}
          <TextField margin="dense" label="URL изображения" fullWidth value={form.image_url} onChange={e => setForm({...form, image_url: e.target.value})} />
          <FormControl fullWidth margin="dense">
            <InputLabel>Товар</InputLabel>
            <Select value={form.product_id} onChange={e => setForm({...form, product_id: e.target.value})}>
              {products.map(p => (<MenuItem key={p.id} value={p.id}>{p.name} (ID {p.id})</MenuItem>))}
            </Select>
          </FormControl>
        </DialogContent>
        <DialogActions><Button onClick={() => setOpen(false)}>Отмена</Button><Button onClick={handleSave} variant="contained">Сохранить</Button></DialogActions>
      </Dialog>
      <Snackbar open={!!snack} autoHideDuration={3000} onClose={() => setSnack(null)}><Alert severity={snack?.severity}>{snack?.text}</Alert></Snackbar>
    </div>
  );
}