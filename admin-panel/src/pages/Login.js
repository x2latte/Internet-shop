import React, { useState } from 'react';
import { TextField, Button, Container, Typography, Paper, Alert } from '@mui/material';
import api from '../Api';

export default function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const formData = new URLSearchParams();
      formData.append('username', username);
      formData.append('password', password);
      const res = await api.post('/auth/login', formData, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      });
      const token = res.data.access_token;
      localStorage.setItem('access_token', token);
      onLogin(token);
    } catch (err) {
      setError('Неверный логин или пароль');
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Paper elevation={3} sx={{ p: 4, mt: 8 }}>
        <Typography variant="h5" align="center">Вход в систему</Typography>
        {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
        <form onSubmit={handleSubmit}>
          <TextField margin="normal" required fullWidth label="Имя пользователя" autoFocus value={username} onChange={e => setUsername(e.target.value)} />
          <TextField margin="normal" required fullWidth label="Пароль" type="password" value={password} onChange={e => setPassword(e.target.value)} />
          <Button type="submit" fullWidth variant="contained" sx={{ mt: 3 }}>Войти</Button>
        </form>
      </Paper>
    </Container>
  );
}
// затычка
// import React from 'react';
// const Login = () => <div>Login Page</div>;
// export default Login;