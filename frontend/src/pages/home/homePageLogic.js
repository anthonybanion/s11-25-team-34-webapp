// ==========================================
//
// Description: Home Page Business Logic
//
// File: homePageLogic.js
// Author: Anthony Bañon
// Created: [Fecha]
// Last Updated: [Fecha]
// ==========================================

import { productService } from '../../services/products/productService';
import { useNotification } from '../../hooks/useNotification';
import { useState, useEffect, useMemo } from 'react';

const STATIC_URL =
  import.meta.env.VITE_STATIC_URL || 'http://localhost:8000/media';

export const useHomePageLogic = () => {
  const { showError } = useNotification();
  const [regularProducts, setRegularProducts] = useState([]);
  const [discountProducts, setDiscountProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await productService.getAll();
        const productsData = response.results || [];

        const transformedProducts = productsData.map((product) => ({
          id: product.id,
          name: product.name,
          imageUrl: product.image_url,
          price: product.price,
          ecoBadge: product.eco_badge,
        }));

        // 🔥 Shuffle function
        const shuffle = (arr) =>
          arr
            .map((value) => ({ value, sort: Math.random() }))
            .sort((a, b) => a.sort - b.sort)
            .map(({ value }) => value);

        // Primer grupo random (descuentos)
        const discountList = shuffle(transformedProducts).slice(0, 8);

        // Segundo grupo random distinto:
        const remaining = transformedProducts.filter(
          (p) => !discountList.some((d) => d.id === p.id)
        );

        const regularList = shuffle(remaining).slice(0, 8);

        setDiscountProducts(discountList);
        setRegularProducts(regularList);
      } catch (error) {
        showError('Failed to load products');
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  return {
    discountProducts,
    regularProducts,
    loading,
  };
};
