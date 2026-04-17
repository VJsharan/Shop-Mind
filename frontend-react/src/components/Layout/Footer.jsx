import { Sparkles, Github, Twitter, Instagram } from 'lucide-react';

export default function Footer() {
  return (
    <footer style={{ borderTop: '1px solid var(--border-color)', backgroundColor: 'var(--bg-secondary)', marginTop: '4rem', padding: '4rem 0 2rem' }}>
      <div className="container">
        <div className="grid grid-cols-4 gap-8 mb-8">
          <div style={{ gridColumn: 'span 2' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '1.5rem', fontWeight: 900, fontFamily: 'var(--font-display)', marginBottom: '1rem' }}>
              <Sparkles className="text-gradient" size={28} />
              <span>Shop<span className="text-gradient">Mind</span></span>
            </div>
            <p style={{ color: 'var(--text-muted)', maxWidth: '400px', marginBottom: '1.5rem' }}>
              The future of e-commerce. AI-powered intelligent shopping assistant that finds exactly what you need in natural language.
            </p>
            <div style={{ display: 'flex', gap: '1rem' }}>
              <a href="#" className="btn-icon"><Twitter size={18} /></a>
              <a href="#" className="btn-icon"><Instagram size={18} /></a>
              <a href="#" className="btn-icon"><Github size={18} /></a>
            </div>
          </div>
          
          <div>
            <h4 style={{ marginBottom: '1.5rem', color: 'var(--text-primary)' }}>Shop</h4>
            <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.75rem', color: 'var(--text-secondary)' }}>
              <li><a href="/products">All Products</a></li>
              <li><a href="/products?category=shirts">Men's Wear</a></li>
              <li><a href="/products?category=dresses">Women's Wear</a></li>
              <li><a href="/products?category=shoes">Footwear</a></li>
            </ul>
          </div>
          
          <div>
            <h4 style={{ marginBottom: '1.5rem', color: 'var(--text-primary)' }}>Company</h4>
            <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.75rem', color: 'var(--text-secondary)' }}>
              <li><a href="#">About Us</a></li>
              <li><a href="#">Contact</a></li>
              <li><a href="#">Privacy Policy</a></li>
              <li><a href="#">Terms of Service</a></li>
            </ul>
          </div>
        </div>
        
        <div style={{ borderTop: '1px solid var(--border-color)', paddingTop: '2rem', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.875rem' }}>
          &copy; {new Date().getFullYear()} ShopMind. All rights reserved. Built with React & FastAPI.
        </div>
      </div>
    </footer>
  );
}
