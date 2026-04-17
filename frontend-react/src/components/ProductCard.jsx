import { Link } from 'react-router-dom';
import { Heart, ShoppingBag, Star } from 'lucide-react';
import { getProductImage } from '../utils/images';
import { useCart } from '../context/CartContext';
import { useWishlist } from '../context/WishlistContext';

export default function ProductCard({ product }) {
  const { addItem } = useCart();
  const { isWishlisted, toggleWishlist } = useWishlist();
  const wishlisted = isWishlisted(product.id);
  
  const handleAddToCart = (e) => {
    e.preventDefault();
    addItem(product, product.sizes?.[0] || null);
  };

  const handleToggleWishlist = (e) => {
    e.preventDefault();
    toggleWishlist(product);
  };

  return (
    <Link to={`/products/${product.id}`} className="product-card">
      <div className="product-image-container">
        <img 
          src={getProductImage(product)} 
          alt={product.name} 
          className="product-image"
          loading="lazy"
        />
        {product.stock < 20 && (
          <div className="product-badge" style={{ color: '#ef4444', borderColor: 'rgba(239, 68, 68, 0.2)' }}>
            Few Left
          </div>
        )}
        
        <div className="product-actions">
          <button 
            className="btn-icon" 
            onClick={handleToggleWishlist}
            style={{ color: wishlisted ? 'var(--accent-secondary)' : 'inherit', borderColor: wishlisted ? 'var(--accent-secondary)' : '' }}
          >
            <Heart size={20} fill={wishlisted ? 'currentColor' : 'none'} />
          </button>
          <button className="btn-icon" onClick={handleAddToCart}>
            <ShoppingBag size={20} />
          </button>
        </div>
      </div>
      
      <div className="product-info">
        <div className="product-brand">{product.brand}</div>
        <h3 className="product-name">{product.name}</h3>
        
        <div className="product-meta">
          <div className="product-price">₹{product.price.toLocaleString()}</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.875rem', color: '#fbbf24' }}>
            <Star size={14} fill="currentColor" />
            <span style={{ color: 'var(--text-secondary)' }}>{product.rating}</span>
          </div>
        </div>
      </div>
    </Link>
  );
}
