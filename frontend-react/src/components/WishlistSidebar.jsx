import { X, ShoppingBag } from 'lucide-react';
import { useWishlist } from '../context/WishlistContext';
import { useCart } from '../context/CartContext';
import { getProductImage } from '../utils/images';
import { Link } from 'react-router-dom';

export default function WishlistSidebar({ isOpen, onClose }) {
  const { items, toggleWishlist } = useWishlist();
  const { addItem } = useCart();

  const handleAddToCart = (product) => {
    addItem(product, product.sizes?.[0] || null);
    toggleWishlist(product); // Remove from wishlist when added to cart
  };

  return (
    <>
      <div className={`sidebar-overlay ${isOpen ? 'open' : ''}`} onClick={onClose} />
      <div className={`sidebar ${isOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <h2 style={{ fontSize: '1.25rem' }}>Wishlist ({items.length})</h2>
          <button className="btn-icon" onClick={onClose}><X size={20} /></button>
        </div>
        
        <div className="sidebar-body">
          {items.length === 0 ? (
            <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '2rem' }}>
              Your wishlist is empty.
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {items.map((product) => (
                <div key={product.id} style={{ display: 'flex', gap: '1rem', background: 'var(--bg-tertiary)', padding: '0.75rem', borderRadius: 'var(--radius-md)' }}>
                  <img 
                    src={getProductImage(product)} 
                    alt={product.name}
                    style={{ width: '80px', height: '100px', objectFit: 'cover', borderRadius: 'var(--radius-sm)' }}
                  />
                  <div style={{ flexGrow: 1, display: 'flex', flexDirection: 'column' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                      <Link to={`/products/${product.id}`} onClick={onClose} style={{ fontSize: '0.875rem', marginBottom: '0.25rem', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden', color: 'var(--text-primary)' }}>
                        {product.name}
                      </Link>
                      <button onClick={() => toggleWishlist(product)} style={{ color: 'var(--text-muted)' }}>
                        <X size={16} />
                      </button>
                    </div>
                    
                    <div style={{ marginTop: 'auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <div style={{ fontWeight: 'bold', color: 'var(--accent-primary)' }}>₹{product.price}</div>
                      
                      <button 
                        className="btn-icon" 
                        onClick={() => handleAddToCart(product)}
                        style={{ background: 'linear-gradient(135deg, var(--accent-primary), var(--accent-secondary))', color: 'white', border: 'none' }}
                      >
                        <ShoppingBag size={16} />
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </>
  );
}
