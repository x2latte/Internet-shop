import api from './axios';

export const login = (username, password) =>
  api.post('/auth/login', new URLSearchParams({ username, password }));

export const getCategories = () => api.get('/categories/');
export const createCategory = (data) => api.post('/categories/', data);
export const updateCategory = (id, data) => api.put(`/categories/${id}`, data);
export const deleteCategory = (id) => api.delete(`/categories/${id}`);

export const getBrands = () => api.get('/brands/');
export const createBrand = (data) => api.post('/brands/', data);
export const updateBrand = (id, data) => api.put(`/brands/${id}`, data);
export const deleteBrand = (id) => api.delete(`/brands/${id}`);

export const getProducts = (params) => api.get('/products/', { params });
export const createProduct = (data) => api.post('/products/', data);
export const updateProduct = (id, data) => api.put(`/products/${id}`, data);
export const deleteProduct = (id) => api.delete(`/products/${id}`);

export const getProductImages = (productId) => api.get(`/images/product/${productId}`);
export const addImage = (productId, imageUrl) =>
  api.post('/images/', { image_url: imageUrl }, { params: { product_id: productId } });
export const deleteImage = (imageId) => api.delete(`/images/${imageId}`);