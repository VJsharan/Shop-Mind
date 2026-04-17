import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ShoppingBag, Heart, Star, ArrowLeft } from 'lucide-react';
import { fetchProductById } from '../api';
import { getProductImage } from '../utils/images';
import { useCart } from '../context/CartContext';
import { useWishlist } from '../context/WishlistContext';

export default function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedSize, setSelectedSize] = useState(null);
  
  const { addItem } = useCart();
  const { isWishlisted, toggleWishlist } = useWishlist();

  useEffect(() => {
    fetchProductById(id).then(data => {
      setProduct(data);
      if (data.sizes?.length) setSelectedSize(data.sizes[0]);
      setLoading(false);
    }).catch(console.error);
  }, [id]);

  if (loading) return <div className="container py-16" style={{ textAlign: 'center', color: 'var(--text-muted)' }}>Loading...</div>;
  if (!product) return <div className="container py-16" style={{ textAlign: 'center', color: 'var(--text-muted)' }}>Product not found.</div>;

  const wishlisted = isWishlisted(product.id);

  return (
    <div className="container py-16 animate-fade-in">
      <Link to="/products" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', color: 'var(--text-secondary)', marginBottom: '2rem' }}>
        <ArrowLeft size={20} /> Back to Catalog
      </Link>
      
      <div className="grid grid-cols-2 gap-8">
        <div style={{ position: 'relative', borderRadius: 'var(--radius-xl)', overflow: 'hidden', border: '1px solid var(--border-color)', aspectRatio: '3/4' }}>
          <img 
            src={getProductImage(product)} 
            alt={product.name}
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        </div>
        
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          <div style={{ textTransform: 'uppercase', letterSpacing: '0.1em', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '0.5rem' }}>
            {product.brand}
          </div>
          
          <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>{product.name}</h1>
          
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '2rem' }}>
            <span style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--accent-primary)', fontFamily: 'var(--font-display)' }}>
              ₹{product.price.toLocaleString()}
            </span>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.25rem', color: '#fbbf24', background: 'var(--bg-secondary)', padding: '0.25rem 0.75rem', borderRadius: 'var(--radius-full)' }}>
              <Star size={16} fill="currentColor" />
              <span style={{ color: 'var(--text-primary)', fontWeight: 600 }}>{product.rating}</span>
            </div>
          </div>
          
          <p style={{ color: 'var(--text-secondary)', fontSize: '1.125rem', lineHeight: 1.6, marginBottom: '2rem' }}>
            {product.description}
          </p>
          
          {product.sizes && product.sizes.length > 0 && product.sizes[0] !== 'one size' && (
            <div style={{ marginBottom: '2rem' }}>
              <h4 style={{ marginBottom: '0.75rem' }}>Select Size</h4>
              <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                {product.sizes.map(size => (
                  <button 
                    key={size}
                    onClick={() => setSelectedSize(size)}
                    style={{ 
                      width: '48px', height: '48px', 
                      borderRadius: 'var(--radius-sm)', 
                      display: 'flex', alignItems: 'center', justifyContent: 'center',
                      fontWeight: 600, textTransform: 'uppercase',
                      background: selectedSize === size ? 'var(--text-primary)' : 'var(--bg-secondary)',
                      color: selectedSize === size ? 'var(--bg-primary)' : 'var(--text-primary)',
                      border: `1px solid ${selectedSize === size ? 'var(--text-primary)' : 'var(--border-color)'}`,
                      transition: 'all 0.2s'
                    }}
                  >
                    {size}
                  </button>
                ))}
              </div>
            </div>
          )}
          
          <div style={{ display: 'flex', gap: '1rem', marginTop: 'auto' }}>
            <button 
              className="btn btn-primary" 
              style={{ flexGrow: 1, padding: '1rem' }}
              onClick={() => addItem(product, selectedSize)}
            >
              <ShoppingBag size={20} /> Add to Cart
            </button>
            <button 
              className="btn-icon" 
              style={{ width: '56px', height: '56px', color: wishlisted ? 'var(--accent-secondary)' : 'inherit', borderColor: wishlisted ? 'var(--accent-secondary)' : '' }}
              onClick={() => toggleWishlist(product)}
            >
              <Heart size={24} fill={wishlisted ? 'currentColor' : 'none'} />
            </button>
          </div>
          
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginTop: '2rem', paddingTop: '2rem', borderTop: '1px solid var(--border-color)' }}>
            <span className="tag">Category: {product.category}</span>
            <span className="tag">Color: {product.color}</span>
            {product.occasion.map(occ => <span key={occ} className="tag">{occ}</span>)}
          </div>
        </div>
      </div>
    </div>
  );
}
