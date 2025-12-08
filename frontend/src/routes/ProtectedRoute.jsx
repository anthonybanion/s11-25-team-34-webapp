// routes/ProtectedRoute.jsx
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export const ProtectedRoute = ({
  children,
  requiredRole,
  redirectTo = '/login',
}) => {
  const { isAuthenticated, role } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to={redirectTo} replace />;
  }

  if (requiredRole && role !== requiredRole) {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
};
