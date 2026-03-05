import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useState } from 'react';
import Error from '../components/Error';
import Loader from '../components/Loader';
import Success from '../components/Success';
import { useParams } from 'react-router-dom';
import { getProductById, updateProduct } from '../redux/product.slice';

export default function EditProduct() {
  const { id } = useParams();
  const productState = useSelector((state) => state.productReducer);
  const { product, error, loading } = productState;
  const updateProductState = useSelector((state) => state.productReducer);
  const {
    success
  } = updateProductState;

  const [name, setName] = useState('');
  const [price, setPrice] = useState('');
  const [countInStock, setCountInStock] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const dispatch = useDispatch();

   function editProduct(e) {
    e.preventDefault();
    const product = {
      id: id,
      name: name,
      image: imageUrl,
      category: category,
      description: description,
      price: price,
      countInStock: countInStock,
      rating: 0
    };
    try {
     dispatch(updateProduct(product));
    }catch (err) {
        console.log(err);
    }
  }

  useEffect(() => {
        if (product) {
          if (id == product.id ) {
            setName(product.name);
            setPrice(product.price);
            setDescription(product.description);
            setImageUrl(product.image);
            setCategory(product.category);
            setCountInStock(product.countInStock);
          } else {
            dispatch(getProductById(id));
          }
        } else {
          dispatch(getProductById(id));
        }
      }, [dispatch, product]);

  return (
    <div className="flex justify-center mt-8">
      <div className="w-full max-w-md bg-white rounded shadow p-6 mb-10">
        <h2 className="text-2xl font-semibold mb-4">Изменение информации о товаре:</h2>
        {loading && <Success success="Product Updated Successfully" />}
        {product && (
          <div>
            <form onSubmit={editProduct}>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2">Название:</label>
                <input
                  type="text"
                  className="form-input w-full"
                  placeholder=""
                  required
                  value={name}
                  onChange={(e) => {
                    setName(e.target.value);
                  }}
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2">Цена</label>
                <input
                  type="number"
                  className="form-input w-full"
                  placeholder="цена в рублях"
                  value={price}
                  required
                  onChange={(e) => {
                    setPrice(e.target.value);
                  }}
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2">
                  Описание
                </label>
                <input
                  type="text"
                  required
                  className="form-input w-full"
                  placeholder=""
                  value={description}
                  onChange={(e) => {
                    setDescription(e.target.value);
                  }}
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2">
                  Image URL
                </label>
                <input
                  type="text"
                  required
                  className="form-input w-full"
                  placeholder="ссылка на изображение товара"
                  value={imageUrl}
                  onChange={(e) => {
                    setImageUrl(e.target.value);
                  }}
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2">
                  Категория
                </label>
                <input
                  type="text"
                  required
                  className="form-input w-full"
                  placeholder=""
                  value={category}
                  onChange={(e) => {
                    setCategory(e.target.value);
                  }}
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-2">
                  Кол-во товара в наличии
                </label>
                <input
                  type="number"
                  required
                  className="form-input w-full"
                  placeholder="0"
                  value={countInStock}
                  onChange={(e) => {
                    setCountInStock(e.target.value);
                  }}
                />
              </div>
              <button
                className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                type="submit"
              >
                Изменить
              </button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
}
