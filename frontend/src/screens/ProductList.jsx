import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Loader from '../components/Loader';
import Error from '../components/Error';
import { Link } from 'react-router-dom';
import { deleteProduct, getAllProducts } from '../redux/product.slice';

export default function ProductList() {
  const dispatch = useDispatch();
  const getallproductsstate = useSelector((state) => state.productReducer);
  const { products, loading, error } = getallproductsstate;

  useEffect(() => {
    dispatch(getAllProducts());
  }, [dispatch]);

  return (
    <div className="relative overflow-x-auto admin-table">
      <h2 className="text-2xl text-center font-semibold mb-4">Список товаров:</h2>
      {loading && <Loader />}
      {error && <Error error="Something went wrong" />}

      <table className="orderTable">
        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" className="px-6 py-4">
              Название товара
            </th>
            <th scope="col" className="px-6 py-4">
              Цена, руб.
            </th>
            <th scope="col" className="px-6 py-4">
              Кол-во в наличии
            </th>
            <th scope="col" className="px-6 py-4">
              Id товара
            </th>
            <th scope="col" className="px-6 py-4">
              Действия
            </th>
          </tr>
        </thead>

        <tbody>
          {products &&
            products.map((product) => {
              return (
                <tr
                  key={product.id}
                  className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                >
                  <td className="px-6 py-4">{product.name}</td>
                  <td className="px-6 py-4">{product.price}</td>
                  <td className="px-6 py-4">{product.countInStock}</td>
                  <td className="px-6 py-4">{product.id}</td>
                  <td className="px-6 py-4">
                    <i
                      className="far fa-trash-alt cursor-pointer mr-2"
                      onClick={() => {
                        dispatch(deleteProduct(product.id));
                      }}
                    ></i>
                    <Link to={`/admin/editproduct/${product.id}`}>
                      <i className="fas fa-edit"></i>
                    </Link>
                  </td>
                </tr>
              );
            })}
        </tbody>
      </table>
    </div>
  );
}
