import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Sparkles } from 'lucide-react';
import { fetchProducts } from '../api';
import ProductCard from '../components/ProductCard';
import { CATEGORY_LABELS, getCategoryImage } from '../utils/images';

export default function Home() {
  const [featuredProducts, setFeaturedProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts(8).then(data => {
      setFeaturedProducts(data);
      setLoading(false);
    }).catch(console.error);
  }, []);

  const categories = ['shirts', 'shoes', 'watches', 'bags'];

  return (
    <div>
      {/* Hero Section */}
      <section style={{ position: 'relative', overflow: 'hidden', padding: '6rem 0', minHeight: '80vh', display: 'flex', alignItems: 'center' }}>
        <div style={{ position: 'absolute', inset: 0, zIndex: -1 }}>
          <div style={{ position: 'absolute', top: '20%', left: '10%', width: '400px', height: '400px', background: 'var(--accent-glow)', filter: 'blur(100px)', borderRadius: '50%' }}></div>
          <div style={{ position: 'absolute', bottom: '10%', right: '10%', width: '500px', height: '500px', background: 'rgba(236, 72, 153, 0.2)', filter: 'blur(120px)', borderRadius: '50%' }}></div>
        </div>

        <div className="container" style={{ position: 'relative', zIndex: 10 }}>
          <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center' }}>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.5rem 1rem', background: 'rgba(255,255,255,0.05)', borderRadius: 'var(--radius-full)', marginBottom: '2rem', border: '1px solid rgba(255,255,255,0.1)' }}>
              <Sparkles size={16} className="text-gradient" />
              <span style={{ fontSize: '0.875rem', fontWeight: 500 }}>Powered by Google Gemini 1.5</span>
            </div>
            
            <h1 style={{ fontSize: '4.5rem', marginBottom: '1.5rem' }}>
              Redefining the <br/>
              <span className="text-gradient">Shopping Experience</span>
            </h1>
            
            <p style={{ fontSize: '1.25rem', color: 'var(--text-secondary)', marginBottom: '3rem', lineHeight: 1.6 }}>
              Tell us what you're looking for in natural language. Our AI understands your style, occasion, and budget to find exactly what you need.
            </p>
            
            <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
              <Link to="/chat" className="btn btn-primary" style={{ padding: '1rem 2rem', fontSize: '1.125rem' }}>
                <Sparkles size={20} /> Try AI Assistant
              </Link>
              <Link to="/products" className="btn btn-secondary" style={{ padding: '1rem 2rem', fontSize: '1.125rem' }}>
                Browse Catalog
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="py-16" style={{ background: 'var(--bg-secondary)' }}>
        <div className="container">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '3rem' }}>
            <div>
              <h2 style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>Shop by Category</h2>
              <p style={{ color: 'var(--text-secondary)' }}>Explore our curated collections.</p>
            </div>
            <Link to="/products" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--accent-primary)', fontWeight: 600 }}>
              View All <ArrowRight size={20} />
            </Link>
          </div>

          <div className="grid grid-cols-4 gap-6">
            {categories.map(cat => (
              <Link to={`/products?category=${cat}`} key={cat} style={{ position: 'relative', borderRadius: 'var(--radius-lg)', overflow: 'hidden', aspectRatio: '4/5', display: 'block', group: 'true' }}>
                <img src={getCategoryImage(cat)} alt={cat} style={{ width: '100%', height: '100%', objectFit: 'cover', transition: 'transform 0.5s' }} />
                <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 50%)' }}></div>
                <h3 style={{ position: 'absolute', bottom: '1.5rem', left: '1.5rem', fontSize: '1.5rem', fontWeight: 700 }}>{CATEGORY_LABELS[cat]}</h3>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16">
        <div className="container">
          <h2 style={{ fontSize: '2.5rem', marginBottom: '3rem', textAlign: 'center' }}>Featured Selection</h2>
          
          {loading ? (
            <div style={{ textAlign: 'center', padding: '4rem 0', color: 'var(--text-muted)' }}>Loading products...</div>
          ) : (
            <div className="grid grid-cols-4 gap-6">
              {featuredProducts.map(product => (
                <ProductCard key={product.id} product={product} />
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
