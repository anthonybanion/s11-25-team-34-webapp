import { ProductCard } from '../../molecules/cards/ProductCard';
import { memo } from 'react';

export const ProductGrid = memo(({ products }) => {
  if (!products) return null;
  console.log('products EN GRID:', products);
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-4 sm:gap-4 lg:gap-8">
      {products.map((product) => (
        <ProductCard
          key={product.id}
          imageSrc={product.imageUrl}
          name={product.name}
          price={product.price}
          ecoBadge={product.ecoBadge}
        />
      ))}
    </div>
  );
});
