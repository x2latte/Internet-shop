import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Loader from '../components/Loader';
import Error from '../components/Error';
import { getOrdersByUserId } from '../redux/order.slice';
import '../App.css';
export default function OrderScreen() {
  const orderState = useSelector((state) => state.orderReducer);

  const { orders, getOrdersByUserIdError, getOrdersByUserIdLoading } =
    orderState;

  const dispatch = useDispatch();

  const currentUser = JSON.parse(localStorage.getItem('currentUser'));

  useEffect(() => {
    if (currentUser) {
      dispatch(getOrdersByUserId(currentUser.id));
    } else {
      window.location.href = '/login';
    }
  }, [dispatch]);

  return (
    <div>
      <div className="flex justify-center mt-5 ">
        <div className="w-3/4">
          <h2 className="text-2xl text-center font-semibold admin-table" >Заказы:</h2>
          <table className="orderTable">
            <thead>
              <tr>
                <th>ID заказа</th>
                <th>Сумма</th>
                <th>Дата</th>
                <th>ID транзакции</th>
                <th>Статус</th>
              </tr>
            </thead>
            <tbody>
              {getOrdersByUserIdLoading && <Loader />}
              {orders &&
                orders.map((order) => {
                  return (
                    <tr
                      key={order.id}
                      onClick={() => {
                        window.location = `/orderinfo/${order.id}`;
                      }}
                    >
                      <td>{order.id}</td>
                      <td>{order.orderAmount}</td>
                      <td>{order.created_at.substring(0, 10)}</td>
                      <td>{order.transactionId}</td>
                      <td>
                        {order.isDelivered ? (
                          <h3 className="md:text-xl font-semibold">Товар доставлен</h3>
                        ) : (
                          <h3 className="md:text-xl font-semibold">Товар в пути</h3>
                        )}
                      </td>
                    </tr>
                  );
                })}
              {getOrdersByUserIdError && <Error error="something went wrong" />}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
