import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children, allowedRoles, userRole }) => {
  if (!userRole) {
    return <Navigate to="/login" />;
  }
  if (!allowedRoles.includes(userRole)) {
    return <Navigate to="/shop" />;
  }
  return children;
};

export default ProtectedRoute;
