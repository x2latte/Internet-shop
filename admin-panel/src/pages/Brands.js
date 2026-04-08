// import React from 'react';

// const Brands = () => {
//   return <div>Brands Page (coming soon)</div>;
// };

// export default Brands;

import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions, Alert, Snackbar } from '@mui/material';
import api from '../Api';

export default function Brands() {
  const [brands, setBrands] = useState([]);
  const [open, setOpen] = useState(false);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState({ name: '' });
  const [error, setError] = useState('');
  const [snack, setSnack] = useState(null);

  const fetchData = async () => {
    const res = await api.get('/brands/');
    setBrands(res.data);
  };

  useEffect(() => { fetchData(); }, []);

  const handleOpen = (item = null) => {
    if (item) { setEditing(item); setForm({ name: item.name }); }
    else { setEditing(null); setForm({ name: '' }); }
    setError('');
    setOpen(true);
  };

  const handleSave = async () => {
    try {
      if (editing) await api.put(`/brands/${editing.id}`, form);
      else await api.post('/brands/', form);
      setSnack({ severity: 'success', text: editing ? 'Обновлено' : 'Создано' });
      fetchData();
      setOpen(false);
    } catch (err) { setError(err.response?.data?.detail || 'Ошибка'); }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Удалить бренд?')) {
      await api.delete(`/brands/${id}`);
      setSnack({ severity: 'info', text: 'Удалено' });
      fetchData();
    }
  };

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'name', headerName: 'Название', width: 200 },
    { field: 'actions', headerName: 'Действия', width: 200, renderCell: (params) => (<><Button size="small" onClick={() => handleOpen(params.row)}>Изменить</Button><Button size="small" color="error" onClick={() => handleDelete(params.row.id)}>Удалить</Button></>) }
  ];

  return (
    <div>
      <Button variant="contained" onClick={() => handleOpen()} sx={{ mb: 2 }}>Добавить бренд</Button>
      <DataGrid rows={brands} columns={columns} autoHeight />
      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>{editing ? 'Изменить' : 'Новый бренд'}</DialogTitle>
        <DialogContent>
          {error && <Alert severity="error">{error}</Alert>}
          <TextField margin="dense" label="Название" fullWidth value={form.name} onChange={e => setForm({...form, name: e.target.value})} />
        </DialogContent>
        <DialogActions><Button onClick={() => setOpen(false)}>Отмена</Button><Button onClick={handleSave} variant="contained">Сохранить</Button></DialogActions>
      </Dialog>
      <Snackbar open={!!snack} autoHideDuration={3000} onClose={() => setSnack(null)}><Alert severity={snack?.severity}>{snack?.text}</Alert></Snackbar>
    </div>
  );
}