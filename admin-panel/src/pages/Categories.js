// import React from 'react';

// const Categories = () => {
//   return <div>Categories Page (coming soon)</div>;
// };

// export default Categories;

import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions, Alert, Snackbar } from '@mui/material';
import api from '../Api';

export default function Categories() {
  const [categories, setCategories] = useState([]);
  const [open, setOpen] = useState(false);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState({ name: '', description: '' });
  const [error, setError] = useState('');
  const [snack, setSnack] = useState(null);

  const fetchData = async () => {
    const res = await api.get('/categories/');
    setCategories(res.data);
  };

  useEffect(() => { fetchData(); }, []);

  const handleOpen = (item = null) => {
    if (item) { setEditing(item); setForm({ name: item.name, description: item.description || '' }); }
    else { setEditing(null); setForm({ name: '', description: '' }); }
    setError('');
    setOpen(true);
  };

  const handleSave = async () => {
    try {
      if (editing) await api.put(`/categories/${editing.id}`, form);
      else await api.post('/categories/', form);
      setSnack({ severity: 'success', text: editing ? 'Обновлено' : 'Создано' });
      fetchData();
      setOpen(false);
    } catch (err) { setError(err.response?.data?.detail || 'Ошибка'); }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Удалить категорию?')) {
      await api.delete(`/categories/${id}`);
      setSnack({ severity: 'info', text: 'Удалено' });
      fetchData();
    }
  };

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'name', headerName: 'Название', width: 200 },
    { field: 'description', headerName: 'Описание', width: 300 },
    { field: 'actions', headerName: 'Действия', width: 200, renderCell: (params) => (<><Button size="small" onClick={() => handleOpen(params.row)}>Изменить</Button><Button size="small" color="error" onClick={() => handleDelete(params.row.id)}>Удалить</Button></>) }
  ];

  return (
    <div>
      <Button variant="contained" onClick={() => handleOpen()} sx={{ mb: 2 }}>Добавить категорию</Button>
      <DataGrid rows={categories} columns={columns} autoHeight />
      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>{editing ? 'Изменить' : 'Новая категория'}</DialogTitle>
        <DialogContent>
          {error && <Alert severity="error">{error}</Alert>}
          <TextField margin="dense" label="Название" fullWidth value={form.name} onChange={e => setForm({...form, name: e.target.value})} />
          <TextField margin="dense" label="Описание" fullWidth value={form.description} onChange={e => setForm({...form, description: e.target.value})} />
        </DialogContent>
        <DialogActions><Button onClick={() => setOpen(false)}>Отмена</Button><Button onClick={handleSave} variant="contained">Сохранить</Button></DialogActions>
      </Dialog>
      <Snackbar open={!!snack} autoHideDuration={3000} onClose={() => setSnack(null)}><Alert severity={snack?.severity}>{snack?.text}</Alert></Snackbar>
    </div>
  );
}