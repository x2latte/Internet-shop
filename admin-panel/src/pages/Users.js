import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions, Alert, Snackbar, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import api from '../Api';

export default function Users() {
  const [users, setUsers] = useState([]);
  const [open, setOpen] = useState(false);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState({ username: '', email: '', password: '', role: 'user' });
  const [error, setError] = useState('');
  const [snack, setSnack] = useState(null);

  const fetchUsers = async () => {
    const res = await api.get('/auth/users');
    setUsers(res.data);
  };

  useEffect(() => { fetchUsers(); }, []);

  const handleOpen = (user = null) => {
    if (user) {
      setEditing(user);
      setForm({ username: user.username, email: user.email, password: '', role: user.role });
    } else {
      setEditing(null);
      setForm({ username: '', email: '', password: '', role: 'user' });
    }
    setError('');
    setOpen(true);
  };

  const handleSave = async () => {
    try {
      if (editing) {
        // обновление пользователя (только роль и email, например)
        await api.put(`/auth/users/${editing.id}`, { email: form.email, role: form.role });
        setSnack({ severity: 'success', text: 'Пользователь обновлён' });
      } else {
        // регистрация нового пользователя
        await api.post('/auth/register', { username: form.username, email: form.email, password: form.password, role: form.role });
        setSnack({ severity: 'success', text: 'Пользователь создан' });
      }
      fetchUsers();
      setOpen(false);
    } catch (err) {
      setError(err.response?.data?.detail || 'Ошибка');
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Удалить пользователя?')) {
      await api.delete(`/auth/users/${id}`);
      setSnack({ severity: 'info', text: 'Пользователь удалён' });
      fetchUsers();
    }
  };

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'username', headerName: 'Логин', width: 150 },
    { field: 'email', headerName: 'Email', width: 200 },
    { field: 'role', headerName: 'Роль', width: 120 },
    {
      field: 'actions',
      headerName: 'Действия',
      width: 200,
      renderCell: (params) => (
        <>
          <Button size="small" onClick={() => handleOpen(params.row)}>Изменить</Button>
          <Button size="small" color="error" onClick={() => handleDelete(params.row.id)}>Удалить</Button>
        </>
      )
    }
  ];

  return (
    <div>
      <Button variant="contained" onClick={() => handleOpen()} sx={{ mb: 2 }}>Добавить пользователя</Button>
      <DataGrid rows={users} columns={columns} autoHeight pageSizeOptions={[5, 10]} />
      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>{editing ? 'Изменить пользователя' : 'Новый пользователь'}</DialogTitle>
        <DialogContent>
          {error && <Alert severity="error">{error}</Alert>}
          {!editing && (
            <>
              <TextField margin="dense" label="Логин" fullWidth value={form.username} onChange={e => setForm({...form, username: e.target.value})} />
              <TextField margin="dense" label="Пароль" type="password" fullWidth value={form.password} onChange={e => setForm({...form, password: e.target.value})} />
            </>
          )}
          <TextField margin="dense" label="Email" fullWidth value={form.email} onChange={e => setForm({...form, email: e.target.value})} />
          <FormControl fullWidth margin="dense">
            <InputLabel>Роль</InputLabel>
            <Select value={form.role} onChange={e => setForm({...form, role: e.target.value})}>
              <MenuItem value="user">Пользователь</MenuItem>
              <MenuItem value="manager">Менеджер</MenuItem>
              <MenuItem value="admin">Администратор</MenuItem>
            </Select>
          </FormControl>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpen(false)}>Отмена</Button>
          <Button onClick={handleSave} variant="contained">Сохранить</Button>
        </DialogActions>
      </Dialog>
      <Snackbar open={!!snack} autoHideDuration={3000} onClose={() => setSnack(null)}><Alert severity={snack?.severity}>{snack?.text}</Alert></Snackbar>
    </div>
  );
}