import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useState } from 'react';
import Navbar from './components/Layout/Navbar';
import Footer from './components/Layout/Footer';
import Home from './pages/Home';
import Products from './pages/Products';
import ProductDetail from './pages/ProductDetail';
import AIChat from './pages/AIChat';
import CartSidebar from './components/CartSidebar';
import WishlistSidebar from './components/WishlistSidebar';

function App() {
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [isWishlistOpen, setIsWishlistOpen] = useState(false);

  return (
    <BrowserRouter>
      <Navbar 
        onOpenCart={() => setIsCartOpen(true)} 
        onOpenWishlist={() => setIsWishlistOpen(true)} 
      />
      
      <main style={{ flexGrow: 1 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<Products />} />
          <Route path="/products/:id" element={<ProductDetail />} />
          <Route path="/chat" element={<AIChat />} />
        </Routes>
      </main>

      <Footer />

      <CartSidebar isOpen={isCartOpen} onClose={() => setIsCartOpen(false)} />
      <WishlistSidebar isOpen={isWishlistOpen} onClose={() => setIsWishlistOpen(false)} />
    </BrowserRouter>
  );
}

export default App;
