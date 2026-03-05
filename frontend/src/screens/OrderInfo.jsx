import { useParams } from 'react-router-dom';
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Loader from '../components/Loader';
import Error from '../components/Error';
import { getOrderById } from '../redux/order.slice';

export default function OrderInfo() {
  const { orderid } = useParams();

  const dispatch = useDispatch();
  const orderState = useSelector((state) => state.orderReducer);

  const { order, getOrderByIdLoading, getOrderByIdError } = orderState;

  useEffect(() => {
    dispatch(getOrderById(orderid));
    console.log(order);
  }, [dispatch]);

  return (
    <div>
      {getOrderByIdError && <Error error="Something went wrong" />}
      {getOrderByIdLoading && <Loader />}
      {order && (
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-white rounded-lg p-4 mx-3 my-3">
            <h2 className="text-xl font-semibold">Товары в заказе:</h2>
            <hr className="my-2" />
            {order.orderItems.map((item) => {
              return (
                <div className="orderitem" key={item._id}>
                  <h1>Название товара: {item.name}</h1>
                  <h1>
                    Количество: <b>{item.quantity}</b>
                  </h1>
                  <h1>
                    Цена: {item.quantity} * {item.price} ={' '}
                    {item.price * item.quantity} рублей.
                  </h1>
                  <hr className="my-2" />
                </div>
              );
            })}
          </div>
          <div className="bg-white rounded-lg p-4 mx-3 my-3">
            <h2 className="text-xl font-semibold">Информация о заказе:</h2>
            <hr className="my-2" />
            <h3>Сумма заказа: {order.orderAmount} рублей.</h3>
            <h3>Дата заказа: {order.created_at.substring(0, 10)}</h3>
            <h3>ID транзакции: {order.transactionId}</h3>
            {order.isDelivered ? (
              <h3 className="text-xl font-semibold">Товар доставлен</h3>
            ) : (
              <h3 className="text-xl font-semibold">Товар в пути</h3>
            )}
            <hr className="my-2" />
            <div className="text-right">
              <h2 className="text-xl font-semibold">Информация о доставке:</h2>
              <hr className="my-2" />
              <h1 className="text-right">
                Адрес получателя: <b>{order.shippingAddress.address}</b>
              </h1>
              <h1 className="text-right">
                Город: <b>{order.shippingAddress.city}</b>
              </h1>
              <h1 className="text-right">
                Страна: <b>{order.shippingAddress.country}</b>
              </h1>
            </div>
          </div>
        </div>
      )}
      <hr className="my-4" />
      <div className="text-center">
        <h2 className="text-xl font-semibold">Replacement Conditions</h2>
        <p className="text-left">
          A free replacement cannot be created for an item which was returned
          and replaced once earlier. If your item is not eligible for free
          replacement due to any reason, you can always return it for a refund.
          If the item has missing parts or accessories, you may try to contact
          the manufacturer for assistance. Manufacturer contact information can
          usually be found on the item packaging or in the paperwork included
          with the item.
        </p>
      </div>
    </div>
  );
}
