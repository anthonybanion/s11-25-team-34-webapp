import { Button } from '../../atoms/button/Button';
import { Paragraph } from '../../atoms/text/Paragraph';
import { FiShoppingCart } from 'react-icons/fi';

export const CardButton = ({ onClick }) => {
  return (
    <Button
      variant="default"
      icon={FiShoppingCart}
      onClick={onClick}
      className=" w-full px-4 h-14 gap-2"
    >
      <Paragraph variant="bold">Sign Up</Paragraph>
    </Button>
  );
};
