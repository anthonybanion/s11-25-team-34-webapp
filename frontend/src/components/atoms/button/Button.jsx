// ==========================================
//
// Description: Button Component
//
// File: Button.jsx
// Author: Anthony Bañon
// Created: 2025-11-14
// Last Updated: 2025-11-14
// ==========================================

export const Button = ({
  children,
  variant = 'default',
  icon: IconComponent,
  iconClassName = 'w-6 h-6 text-primary',
  className = '',
  ...props
}) => {
  const baseStyles =
    'flex justify-center items-center font-instrument-sans font-semibold rounded-4xl border-2 border-primary transition-colors text-xl text-text-primary';
  // Define variant styles
  const variants = {
    default:
      ' hover:bg-[var(--color-text-placeholder)] focus:bg-[var(--color-text-placeholder)] active:bg-[var(--color-text-placeholder)]',
  };

  const isIconButton = !children && IconComponent;
  const buttonVariant = isIconButton ? 'ghost' : variant;

  return (
    <button
      className={`${baseStyles} ${variants[buttonVariant]} ${className}`}
      {...props}
    >
      {IconComponent && <IconComponent className={iconClassName} />}
      {children}
    </button>
  );
};
