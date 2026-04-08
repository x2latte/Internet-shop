// import api from './axios';

// export const login = (username, password) =>
//   api.post('/auth/login', new URLSearchParams({ username, password }));

// export const getCategories = () => api.get('/categories/');
// export const createCategory = (data) => api.post('/categories/', data);
// export const updateCategory = (id, data) => api.put(`/categories/${id}`, data);
// export const deleteCategory = (id) => api.delete(`/categories/${id}`);

// export const getBrands = () => api.get('/brands/');
// export const createBrand = (data) => api.post('/brands/', data);
// export const updateBrand = (id, data) => api.put(`/brands/${id}`, data);
// export const deleteBrand = (id) => api.delete(`/brands/${id}`);

// export const getProducts = (params) => api.get('/products/', { params });
// export const createProduct = (data) => api.post('/products/', data);
// export const updateProduct = (id, data) => api.put(`/products/${id}`, data);
// export const deleteProduct = (id) => api.delete(`/products/${id}`);

// export const getProductImages = (productId) => api.get(`/images/product/${productId}`);
// export const addImage = (productId, imageUrl) =>
//   api.post('/images/', { image_url: imageUrl }, { params: { product_id: productId } });
// export const deleteImage = (imageId) => api.delete(`/images/${imageId}`);

// export const getMyOrders = () => api.get('/orders/');  // заказы текущего пользователя
// export const getAllOrders = () => api.get('/orders/admin/all'); // все заказы (только админ/менеджер)
// export const updateOrderStatus = (orderId, status) => api.put(`/orders/${orderId}/status`, { status });
// export const getOrderDetails = (orderId) => api.get(`/orders/${orderId}`)

import api from './axios';

// Auth
export const login = (username, password) =>
  api.post('/auth/login', new URLSearchParams({ username, password }));

// Categories
export const getCategories = () => api.get('/categories/');
export const createCategory = (data) => api.post('/categories/', data);
export const updateCategory = (id, data) => api.put(`/categories/${id}`, data);
export const deleteCategory = (id) => api.delete(`/categories/${id}`);

// Brands
export const getBrands = () => api.get('/brands/');
export const createBrand = (data) => api.post('/brands/', data);
export const updateBrand = (id, data) => api.put(`/brands/${id}`, data);
export const deleteBrand = (id) => api.delete(`/brands/${id}`);

// Products
export const getProducts = (params) => api.get('/products/', { params });
export const createProduct = (data) => api.post('/products/', data);
export const updateProduct = (id, data) => api.put(`/products/${id}`, data);
export const deleteProduct = (id) => api.delete(`/products/${id}`);

// Images
export const getProductImages = (productId) => api.get(`/images/product/${productId}`);
export const addImage = (productId, imageUrl) =>
  api.post('/images/', { image_url: imageUrl }, { params: { product_id: productId } });
export const deleteImage = (imageId) => api.delete(`/images/${imageId}`);

// Orders

export const getMyOrders = () => api.get('/orders/');
export const getAllOrders = () => api.get('/orders/admin/all');
export const updateOrderStatus = (orderId, status) => api.put(`/orders/${orderId}/status`, { status });
export const getOrderDetails = (orderId) => api.get(`/orders/${orderId}`);
export const deleteOrder = (orderId) => api.delete(`/orders/${orderId}`);

export default api;