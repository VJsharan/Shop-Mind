import { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { Filter, Search } from 'lucide-react';
import { fetchProducts } from '../api';
import ProductCard from '../components/ProductCard';
import { CATEGORY_LABELS } from '../utils/images';

export default function Products() {
  const [searchParams, setSearchParams] = useSearchParams();
  const initialCategory = searchParams.get('category') || 'all';
  
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState(initialCategory);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetchProducts(50).then(data => {
      setProducts(data);
      setLoading(false);
    }).catch(console.error);
  }, []);

  const filteredProducts = products.filter(p => {
    if (category !== 'all' && p.category !== category) return false;
    if (searchQuery && !p.name.toLowerCase().includes(searchQuery.toLowerCase()) && !p.brand.toLowerCase().includes(searchQuery.toLowerCase())) return false;
    return true;
  });

  const categories = ['all', ...Array.from(new Set(products.map(p => p.category)))];

  return (
    <div className="container py-16 animate-fade-in">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '3rem', marginBottom: '0.5rem' }}>Catalog</h1>
          <p style={{ color: 'var(--text-secondary)' }}>Showing {filteredProducts.length} products</p>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '2rem', alignItems: 'center', marginBottom: '3rem', background: 'var(--bg-secondary)', padding: '1rem', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-color)' }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', flexGrow: 1 }}>
          {categories.map(cat => (
            <button 
              key={cat} 
              onClick={() => {
                setCategory(cat);
                setSearchParams(cat === 'all' ? {} : { category: cat });
              }}
              className="tag"
              style={{ 
                background: category === cat ? 'var(--accent-primary)' : 'var(--bg-tertiary)',
                color: category === cat ? 'white' : 'var(--text-secondary)',
                borderColor: category === cat ? 'var(--accent-primary)' : 'var(--border-color)',
                cursor: 'pointer'
              }}
            >
              {cat === 'all' ? 'All' : CATEGORY_LABELS[cat] || cat}
            </button>
          ))}
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', background: 'var(--bg-tertiary)', padding: '0.5rem 1rem', borderRadius: 'var(--radius-full)', border: '1px solid var(--border-color)' }}>
          <Search size={18} color="var(--text-muted)" />
          <input 
            type="text" 
            placeholder="Search catalog..." 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ background: 'transparent', border: 'none', color: 'var(--text-primary)', outline: 'none', width: '200px' }}
          />
        </div>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '4rem 0', color: 'var(--text-muted)' }}>Loading catalog...</div>
      ) : filteredProducts.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '4rem 0', color: 'var(--text-muted)' }}>No products found matching your criteria.</div>
      ) : (
        <div className="grid grid-cols-4 gap-6">
          {filteredProducts.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      )}
    </div>
  );
}
