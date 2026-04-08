// import React, { useState, useEffect } from 'react';
// import {
//   Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
//   Paper, Button, TextField, IconButton, Dialog, DialogTitle, DialogContent,
//   DialogActions, Box, Typography
// } from '@mui/material';
// import { Edit, Delete, Add, Image } from '@mui/icons-material';
// import { getProducts, createProduct, updateProduct, deleteProduct } from '../api';
// import { useNavigate } from 'react-router-dom';

// const Products = () => {
//   const [products, setProducts] = useState([]);
//   const [open, setOpen] = useState(false);
//   const [editing, setEditing] = useState(null);
//   const [form, setForm] = useState({ name: '', description: '', price: '', category_id: '', brand_id: '' });
//   const [search, setSearch] = useState('');
//   const navigate = useNavigate();

//   const fetchProducts = async () => {
//     try {
//       const res = await getProducts({ search });
//       setProducts(res.data);
//     } catch (err) {
//       console.error(err);
//     }
//   };

//   useEffect(() => {
//     fetchProducts();
//   }, [search]);

//   const handleOpen = (product = null) => {
//     if (product) {
//       setEditing(product);
//       setForm(product);
//     } else {
//       setEditing(null);
//       setForm({ name: '', description: '', price: '', category_id: '', brand_id: '' });
//     }
//     setOpen(true);
//   };

//   const handleClose = () => {
//     setOpen(false);
//     setEditing(null);
//   };

//   const handleSubmit = async () => {
//     try {
//       if (editing) {
//         await updateProduct(editing.id, form);
//       } else {
//         await createProduct(form);
//       }
//       fetchProducts();
//       handleClose();
//     } catch (err) {
//       console.error(err);
//     }
//   };

//   const handleDelete = async (id) => {
//     if (window.confirm('Are you sure?')) {
//       await deleteProduct(id);
//       fetchProducts();
//     }
//   };

//   const handleImages = (productId) => {
//     navigate(`/images/${productId}`);
//   };

//   return (
//     <Box>
//       <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
//         <TextField label="Search" value={search} onChange={(e) => setSearch(e.target.value)} />
//         <Button variant="contained" startIcon={<Add />} onClick={() => handleOpen()}>Add Product</Button>
//       </Box>
//       <TableContainer component={Paper}>
//         <Table>
//           <TableHead>
//             <TableRow>
//               <TableCell>ID</TableCell>
//               <TableCell>Name</TableCell>
//               <TableCell>Price</TableCell>
//               <TableCell>Actions</TableCell>
//             </TableRow>
//           </TableHead>
//           <TableBody>
//             {products.map((p) => (
//               <TableRow key={p.id}>
//                 <TableCell>{p.id}</TableCell>
//                 <TableCell>{p.name}</TableCell>
//                 <TableCell>{p.price}</TableCell>
//                 <TableCell>
//                   <IconButton onClick={() => handleOpen(p)}><Edit /></IconButton>
//                   <IconButton onClick={() => handleDelete(p.id)}><Delete /></IconButton>
//                   <IconButton onClick={() => handleImages(p.id)}><Image /></IconButton>
//                 </TableCell>
//               </TableRow>
//             ))}
//           </TableBody>
//         </Table>
//       </TableContainer>

//       <Dialog open={open} onClose={handleClose}>
//         <DialogTitle>{editing ? 'Edit Product' : 'Add Product'}</DialogTitle>
//         <DialogContent>
//           <TextField margin="dense" label="Name" fullWidth value={form.name} onChange={(e) => setForm({...form, name: e.target.value})} />
//           <TextField margin="dense" label="Description" fullWidth multiline rows={3} value={form.description} onChange={(e) => setForm({...form, description: e.target.value})} />
//           <TextField margin="dense" label="Price" type="number" fullWidth value={form.price} onChange={(e) => setForm({...form, price: e.target.value})} />
//           <TextField margin="dense" label="Category ID" type="number" fullWidth value={form.category_id} onChange={(e) => setForm({...form, category_id: e.target.value})} />
//           <TextField margin="dense" label="Brand ID" type="number" fullWidth value={form.brand_id} onChange={(e) => setForm({...form, brand_id: e.target.value})} />
//         </DialogContent>
//         <DialogActions>
//           <Button onClick={handleClose}>Cancel</Button>
//           <Button onClick={handleSubmit} variant="contained">Save</Button>
//         </DialogActions>
//       </Dialog>
//     </Box>
//   );
// };

// export default Products;


// // // import React from 'react';

// // // const Products = () => {
// // //   return <div>Products page works!</div>;
// // // };

// // // export default Products;

// // затычка
// // import React from 'react';
// // const Products = () => <div>Products Page</div>;
// // export default Products;

// import React, { useState, useEffect } from 'react';
// import {
//   Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
//   Paper, Button, TextField, IconButton, Dialog, DialogTitle, DialogContent,
//   DialogActions, Box, Typography
// } from '@mui/material';
// import { Edit, Delete, Add, Image } from '@mui/icons-material';
// import { getProducts, createProduct, updateProduct, deleteProduct } from '../api';
// import { useNavigate } from 'react-router-dom';
import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions, Alert, Snackbar } from '@mui/material';
import api from '../Api';

export default function Products() {
  const [products, setProducts] = useState([]);
  const [open, setOpen] = useState(false);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState({ name: '', description: '', price: '', category_id: '', brand_id: '' });
  const [error, setError] = useState('');
  const [snack, setSnack] = useState(null);

  const fetchProducts = async () => {
    const res = await api.get('/products/');
    setProducts(res.data);
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleOpen = (product = null) => {
    if (product) {
      setEditing(product);
      setForm({ name: product.name, description: product.description, price: product.price, category_id: product.category_id, brand_id: product.brand_id });
    } else {
      setEditing(null);
      setForm({ name: '', description: '', price: '', category_id: '', brand_id: '' });
    }
    setError('');
    setOpen(true);
  };

  const handleClose = () => setOpen(false);

  const handleSave = async () => {
    try {
      if (editing) {
        await api.put(`/products/${editing.id}`, form);
        setSnack({ severity: 'success', text: 'Товар обновлён' });
      } else {
        await api.post('/products/', form);
        setSnack({ severity: 'success', text: 'Товар создан' });
      }
      fetchProducts();
      handleClose();
    } catch (err) {
      setError(err.response?.data?.detail || 'Ошибка');
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Удалить товар?')) {
      await api.delete(`/products/${id}`);
      setSnack({ severity: 'info', text: 'Товар удалён' });
      fetchProducts();
    }
  };

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'name', headerName: 'Название', width: 200 },
    { field: 'price', headerName: 'Цена', width: 130, valueFormatter: (params) => `${params.value} ₽` },
    { field: 'category_id', headerName: 'Category ID', width: 100 },
    { field: 'brand_id', headerName: 'Brand ID', width: 100 },
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
      <Button variant="contained" onClick={() => handleOpen()} sx={{ mb: 2 }}>Добавить товар</Button>
      <DataGrid rows={products} columns={columns} autoHeight pageSizeOptions={[5, 10]} initialState={{ pagination: { paginationModel: { pageSize: 5 } } }} />
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>{editing ? 'Изменить товар' : 'Новый товар'}</DialogTitle>
        <DialogContent>
          {error && <Alert severity="error">{error}</Alert>}
          <TextField margin="dense" label="Название" fullWidth value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} />
          <TextField margin="dense" label="Описание" fullWidth value={form.description} onChange={e => setForm({ ...form, description: e.target.value })} />
          <TextField margin="dense" label="Цена" type="number" fullWidth value={form.price} onChange={e => setForm({ ...form, price: e.target.value })} />
          <TextField margin="dense" label="ID категории" type="number" fullWidth value={form.category_id} onChange={e => setForm({ ...form, category_id: e.target.value })} />
          <TextField margin="dense" label="ID бренда" type="number" fullWidth value={form.brand_id} onChange={e => setForm({ ...form, brand_id: e.target.value })} />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Отмена</Button>
          <Button onClick={handleSave} variant="contained">Сохранить</Button>
        </DialogActions>
      </Dialog>
      <Snackbar open={!!snack} autoHideDuration={3000} onClose={() => setSnack(null)} anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}>
        <Alert severity={snack?.severity}>{snack?.text}</Alert>
      </Snackbar>
    </div>
  );
}