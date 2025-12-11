import { Button } from '../../atoms/button/Button';
import { IoHomeSharp } from 'react-icons/io5';


export const HomeIcon = ({ onToggle }) => {
  return (
    <Button icon={IoHomeSharp} onClick={onToggle} variant="ghost" className=" p-2" />
  );
};
