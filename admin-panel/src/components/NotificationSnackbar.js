import React, { useState, useEffect } from 'react';
import { Snackbar, Alert } from '@mui/material';

export default function NotificationSnackbar({ message, onClose }) {
  return (
    <Snackbar open={!!message} autoHideDuration={6000} onClose={onClose}
              anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}>
      <Alert onClose={onClose} severity="info" sx={{ width: '100%' }}>
        {message}
      </Alert>
    </Snackbar>
  );
}