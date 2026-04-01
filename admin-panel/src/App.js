// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useState } from 'react';
import Login from './pages/Login';
import Products from './pages/Products';
import Categories from './pages/Categories';
import Brands from './pages/Brands';
import Images from './pages/Images';
import PrivateRoute from './components/PrivateRoute';
import Layout from './components/Layout';

function App() {
  const [isAuth, setIsAuth] = useState(!!localStorage.getItem('token'));

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login setAuth={setIsAuth} />} />
        <Route element={<PrivateRoute isAuth={isAuth} />}>
          <Route element={<Layout />}>
            <Route path="/products" element={<Products />} />
            <Route path="/categories" element={<Categories />} />
            <Route path="/brands" element={<Brands />} />
            <Route path="/images/:productId" element={<Images />} />
            <Route path="/" element={<Navigate to="/products" />} />
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;