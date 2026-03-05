import { useEffect } from 'react';
import { Link, Outlet } from 'react-router-dom';
import HomeScreen from "./Home.jsx";

export default function AdminScreen() {
  const currentUser = JSON.parse(localStorage.getItem('currentUser'));

  useEffect(() => {
    if (currentUser) {
      if (currentUser.role !== "admin" && currentUser.role !== "manager") {
        window.location.href = '/';
      }
    } else {
      window.location.href = '/';
    }
  }, []);

  return (
      <div className="mt-3">
          {!currentUser || (currentUser.role !== "admin" && currentUser.role !== "manager") ? (
              <HomeScreen/>
          ) : (
          <div className="flex justify-center">
            <div className="w-3/4">
              <h2 className="text-2xl font-semibold text-center mb-4">
                Панель администратора
              </h2>
              <ul className="admin p-2 bg-gray-100 rounded flex space-x-2">
                { (currentUser.role === "admin") ?
                <li>
                  <Link
                    to="/admin/userslist"
                    className="text-black block py-2 px-4 hover:bg-gray-200 rounded"
                  >
                    Пользователи
                  </Link>
                </li>
                : ""
                }
                <li>
                  <Link
                    to="/admin/productslist"
                    className="text-black block py-2 px-4 hover:bg-gray-200 rounded"
                  >
                    Товары
                  </Link>
                </li>
                <li>
                  <Link
                    to="/admin/addnewproduct"
                    className="text-black block py-2 px-4 hover:bg-gray-200 rounded"
                  >
                    Добавить товар
                  </Link>
                </li>
                <li>
                  <Link
                    to="/admin/orderslist"
                    className="text-black block py-2 px-4 hover:bg-gray-200 rounded"
                  >
                    Заказы
                  </Link>
                </li>
              </ul>

              <Outlet />
            </div>
          </div>)}
      </div>
  )
}
