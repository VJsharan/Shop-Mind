import { useState, useRef, useEffect } from 'react';
import { Send, Sparkles, Bot, User, ShoppingBag } from 'lucide-react';
import { chatQuery } from '../api';
import ProductCard from '../components/ProductCard';

export default function AIChat() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'bot',
      content: "Hi! I'm ShopMind, your AI shopping assistant. Describe what you're looking for (e.g., 'I need a formal blue shirt under 1500 for an interview') and I'll find the best options for you.",
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);
  
  // Basic session ID for the backend
  const sessionId = useRef(Math.random().toString(36).substring(7)).current;

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const query = input.trim();
    setInput('');
    
    // Add user message
    setMessages(prev => [...prev, { id: Date.now(), role: 'user', content: query }]);
    setLoading(true);

    try {
      const response = await chatQuery(query, sessionId);
      
      setMessages(prev => [...prev, { 
        id: Date.now() + 1, 
        role: 'bot', 
        content: response.summary,
        results: response.results
      }]);
    } catch (error) {
      setMessages(prev => [...prev, { 
        id: Date.now() + 1, 
        role: 'bot', 
        content: "Sorry, I'm having trouble connecting to my servers right now. Please try again later."
      }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container py-8">
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ display: 'inline-flex', alignItems: 'center', gap: '0.75rem', fontSize: '2.5rem' }}>
          <Sparkles className="text-gradient" size={32} />
          ShopMind Assistant
        </h1>
        <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>Powered by Gemini AI</p>
      </div>

      <div className="chat-container">
        <div className="chat-messages">
          {messages.map((msg) => (
            <div key={msg.id} className={`message ${msg.role} animate-fade-in`}>
              <div className="message-avatar">
                {msg.role === 'bot' ? <Bot size={24} /> : <User size={24} />}
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', maxWidth: '100%' }}>
                <div className="message-content">
                  {msg.content}
                </div>
                
                {msg.results && msg.results.length > 0 && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginTop: '0.5rem' }}>
                    {msg.results.slice(0, 3).map((res, idx) => (
                      <div key={res.product.id} style={{ display: 'flex', gap: '1rem', background: 'var(--bg-tertiary)', padding: '1rem', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-color)' }}>
                        <div style={{ width: '80px', flexShrink: 0 }}>
                          <ProductCard product={res.product} />
                        </div>
                        <div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
                            <span style={{ fontSize: '0.75rem', fontWeight: 600, padding: '0.25rem 0.5rem', background: 'rgba(139, 92, 246, 0.2)', color: 'var(--accent-primary)', borderRadius: 'var(--radius-full)' }}>
                              Match: {Math.round(res.relevance_score * 100)}%
                            </span>
                          </div>
                          <h4 style={{ fontSize: '1rem', marginBottom: '0.5rem' }}>{res.product.name}</h4>
                          <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>{res.explanation}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}
          
          {loading && (
            <div className="message bot animate-fade-in">
              <div className="message-avatar animate-pulse">
                <Sparkles size={24} />
              </div>
              <div className="message-content">
                <span className="animate-pulse">Thinking...</span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <form onSubmit={handleSubmit} className="chat-input-area">
          <div className="chat-input-wrapper">
            <input 
              type="text" 
              className="chat-input" 
              placeholder="Ask me to find anything..." 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              disabled={loading}
            />
            <button type="submit" className="chat-submit" disabled={!input.trim() || loading}>
              <Send size={20} />
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
