// ==========================================
//
// Description: Title
//
// File: Title.jsx
// Author: Anthony Bañon
// Created: 2025-11-09
// Last Updated: 2025-11-09
// ==========================================

export const Title = ({
  children,
  variant = 'title',
  className = '',
  ...props
}) => {
  // Base styles
  const baseStyles = 'font-inter font-semibold text-text-primary';
  // Define variant styles
  const variants = {
    brand: 'text-xl',
    title: 'text-2xl font-bold sm:text-3xl',
    subtitle: 'text-lg sm:text-3xl',
  };
  // Determine the HTML tag based on variant
  const Tag = variant === 'title' ? 'h1' : 'h2';

  return (
    <Tag
      className={`${baseStyles} ${variants[variant]} ${className}`}
      {...props}
    >
      {children}
    </Tag>
  );
};
