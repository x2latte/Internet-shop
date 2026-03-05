import { useDispatch, useSelector } from 'react-redux';
import {
  removeFromCart,
  updateCartQuantity,
} from '../redux/cart.slice';
import Checkout from '../components/Checkout';

export default function CartScreen() {
  const cartreducerstate = useSelector((state) => state.cartReducer);
  const dispatch = useDispatch();
  const { cartItems } = cartreducerstate;

  var subtotal = cartItems.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );

  return (
    <div className="relative overflow-x-auto">
      <div className="flex justify-center">
        <div className="w-full md:w-2/3 card text-center shadow p-3 mb-5 my-5 bg-white rounded">
          <div className="text-center mb-5 text-2xl">Товары в корзине:</div>
          <div className="overflow-x-auto">
            <table className="table-auto w-full">
              <thead>
                <tr>
                  <th>Название товара</th>
                  <th>Цена</th>
                  <th>Количество</th>
                  <th>Цена за товар</th>
                  <th>Удалить из корзины</th>
                </tr>
              </thead>
              <tbody>
                {cartItems.map((item) => {
                  return (
                    <tr key={item.id}>
                      {' '}
                      <td>{item.name}</td>
                      <td>{item.price}</td>
                      <td>
                        <input
                          type="number"
                          min="0"
                          value={item.quantity}
                          onChange={(e) =>
                            dispatch(
                              updateCartQuantity({
                                id: item.id,
                                quantity: parseInt(e.target.value),
                              })
                            )
                          }
                        />
                      </td>
                      <td>{item.quantity * item.price}</td>
                      <td>
                        <i
                          style={{ color: 'red' }}
                          className="far fa-trash-alt"
                          onClick={() => {
                            dispatch(removeFromCart(item));
                          }}
                        ></i>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
          <hr />
          <h2 className="text-center mt-10 mb-5">Итого: {subtotal} рублей</h2>
          <hr />
          <Checkout amount={subtotal} />
        </div>
      </div>
    </div>
  );
}
