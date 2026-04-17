import { Link } from 'react-router-dom';
import { useCart } from '../../context/CartContext';
import { useWishlist } from '../../context/WishlistContext';
import { ShoppingBag, Heart, Sparkles, Search } from 'lucide-react';

export default function Navbar({ onOpenCart, onOpenWishlist }) {
  const { totalItems } = useCart();
  const { count: wishlistCount } = useWishlist();

  return (
    <header className="navbar glass">
      <div className="container nav-container">
        <Link to="/" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '1.5rem', fontWeight: 900, fontFamily: 'var(--font-display)' }}>
          <Sparkles className="text-gradient" size={28} />
          <span>Shop<span className="text-gradient">Mind</span></span>
        </Link>

        <nav className="nav-links">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/products" className="nav-link">Catalog</Link>
          <Link to="/chat" className="nav-link" style={{ display: 'flex', alignItems: 'center', gap: '0.25rem', color: 'var(--accent-primary)' }}>
            <Sparkles size={16} /> AI Assistant
          </Link>
        </nav>

        <div className="nav-actions">
          <Link to="/products" className="btn-icon">
            <Search size={20} />
          </Link>
          
          <button className="btn-icon" onClick={onOpenWishlist} style={{ position: 'relative' }}>
            <Heart size={20} />
            {wishlistCount > 0 && <span className="badge-counter">{wishlistCount}</span>}
          </button>
          
          <button className="btn-icon" onClick={onOpenCart} style={{ position: 'relative' }}>
            <ShoppingBag size={20} />
            {totalItems > 0 && <span className="badge-counter">{totalItems}</span>}
          </button>
        </div>
      </div>
    </header>
  );
}
