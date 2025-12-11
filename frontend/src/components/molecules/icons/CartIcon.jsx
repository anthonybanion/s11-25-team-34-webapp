import { Button } from '../../atoms/button/Button';
import { LuShoppingCart } from 'react-icons/lu';

export const CartIcon = ({ onToggle }) => {
  return (
    <Button
      icon={LuShoppingCart}
      iconClassName="text-text-primary group-hover:text-white"
      onClick={onToggle}
      variant="ghost"
      className="group p-2"
    />
  );
};
