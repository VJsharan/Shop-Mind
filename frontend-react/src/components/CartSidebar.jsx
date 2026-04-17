import { X, Trash2, Plus, Minus } from 'lucide-react';
import { useCart } from '../context/CartContext';
import { getProductImage } from '../utils/images';

export default function CartSidebar({ isOpen, onClose }) {
  const { items, updateQuantity, removeItem, totalPrice } = useCart();

  return (
    <>
      <div className={`sidebar-overlay ${isOpen ? 'open' : ''}`} onClick={onClose} />
      <div className={`sidebar ${isOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <h2 style={{ fontSize: '1.25rem' }}>Your Cart ({items.length})</h2>
          <button className="btn-icon" onClick={onClose}><X size={20} /></button>
        </div>
        
        <div className="sidebar-body">
          {items.length === 0 ? (
            <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '2rem' }}>
              Your cart is empty.
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {items.map((item) => (
                <div key={`${item.product.id}-${item.size}`} style={{ display: 'flex', gap: '1rem', background: 'var(--bg-tertiary)', padding: '0.75rem', borderRadius: 'var(--radius-md)' }}>
                  <img 
                    src={getProductImage(item.product)} 
                    alt={item.product.name}
                    style={{ width: '80px', height: '100px', objectFit: 'cover', borderRadius: 'var(--radius-sm)' }}
                  />
                  <div style={{ flexGrow: 1, display: 'flex', flexDirection: 'column' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                      <h4 style={{ fontSize: '0.875rem', marginBottom: '0.25rem', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
                        {item.product.name}
                      </h4>
                      <button onClick={() => removeItem(item.product.id)} style={{ color: 'var(--text-muted)' }}>
                        <Trash2 size={16} />
                      </button>
                    </div>
                    {item.size && <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Size: {item.size}</div>}
                    
                    <div style={{ marginTop: 'auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <div style={{ fontWeight: 'bold', color: 'var(--accent-primary)' }}>₹{item.product.price}</div>
                      
                      <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', background: 'var(--bg-secondary)', borderRadius: 'var(--radius-full)', padding: '0.25rem' }}>
                        <button onClick={() => updateQuantity(item.product.id, item.quantity - 1)} style={{ width: '24px', height: '24px', display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: '50%', background: 'var(--bg-tertiary)' }}><Minus size={12} /></button>
                        <span style={{ fontSize: '0.875rem', minWidth: '1rem', textAlign: 'center' }}>{item.quantity}</span>
                        <button onClick={() => updateQuantity(item.product.id, item.quantity + 1)} style={{ width: '24px', height: '24px', display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: '50%', background: 'var(--bg-tertiary)' }}><Plus size={12} /></button>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
        
        {items.length > 0 && (
          <div className="sidebar-footer">
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem', fontSize: '1.125rem', fontWeight: 'bold' }}>
              <span>Total:</span>
              <span style={{ color: 'var(--accent-primary)' }}>₹{totalPrice.toLocaleString()}</span>
            </div>
            <button className="btn btn-primary" style={{ width: '100%' }}>
              Proceed to Checkout
            </button>
          </div>
        )}
      </div>
    </>
  );
}
