import { HomeTemplate } from '../../components/templates/home_layout/HomeTemplate';
import { ProductGrid } from '../../components/organisms/product_grid/ProductGrid';
import { DiscountProductGrid } from '../../components/organisms/product_grid/DiscountProductGrid';
import { useHomePageLogic } from './homePageLogic';
import homeImage from '../../assets/images/home.jpg';
import { useMemo } from 'react';

export default function HomePage() {
  // Use custom hook for home page logic
  const { discountProducts, regularProducts, loading } = useHomePageLogic();

  const DiscountProductContent = useMemo(
    () => <DiscountProductGrid products={discountProducts} />,
    [discountProducts]
  );

  const productContent = useMemo(
    () => <ProductGrid products={regularProducts} />,
    [regularProducts]
  );
  return (
    <div>
      <HomeTemplate
        homeImage={homeImage}
        discountProductContent={DiscountProductContent}
        productContent={productContent}
        isLoading={loading}
      />
    </div>
  );
}
