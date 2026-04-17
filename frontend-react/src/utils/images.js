const CATEGORY_IMAGES = {
  shirts: [
    'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1598033129183-c4f50c736c10?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1563389234808-52344934935c?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1588359348347-9bc6cbbb689e?w=400&h=500&fit=crop',
  ],
  trousers: [
    'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=500&fit=crop',
  ],
  shoes: [
    'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?w=400&h=500&fit=crop',
  ],
  tshirts: [
    'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1562157873-818bc0726f68?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1503341504253-dff4815485f1?w=400&h=500&fit=crop',
  ],
  jackets: [
    'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1544923246-77307dd270b1?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1548883354-94bcfe321cbb?w=400&h=500&fit=crop',
  ],
  watches: [
    'https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1539874754764-5a96559165b0?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1533139502658-0198f920d8e8?w=400&h=500&fit=crop',
  ],
  bags: [
    'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400&h=500&fit=crop',
  ],
  sunglasses: [
    'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1577803645773-f96470509666?w=400&h=500&fit=crop',
  ],
  dresses: [
    'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&h=500&fit=crop',
  ],
  kurta: [
    'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=400&h=500&fit=crop',
  ],
  ethnic: [
    'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=400&h=500&fit=crop',
  ],
  shorts: [
    'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1562886889-41c1e44bfbee?w=400&h=500&fit=crop',
  ],
  trackpants: [
    'https://images.unsplash.com/photo-1515586838455-8f8f940d6853?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1556906781-9a412961c28c?w=400&h=500&fit=crop',
  ],
  belts: [
    'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1624222247344-550fb60583dc?w=400&h=500&fit=crop',
  ],
  wallets: [
    'https://images.unsplash.com/photo-1627123424574-724758594e93?w=400&h=500&fit=crop',
    'https://images.unsplash.com/photo-1559496417-e7f25cb247f3?w=400&h=500&fit=crop',
  ],
};

const CATEGORY_COVER = {
  shirts: 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=600&h=400&fit=crop',
  trousers: 'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600&h=400&fit=crop',
  shoes: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&h=400&fit=crop',
  tshirts: 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=600&h=400&fit=crop',
  jackets: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&h=400&fit=crop',
  watches: 'https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=600&h=400&fit=crop',
  bags: 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=600&h=400&fit=crop',
  sunglasses: 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=600&h=400&fit=crop',
  dresses: 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600&h=400&fit=crop',
  kurta: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=600&h=400&fit=crop',
  ethnic: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=600&h=400&fit=crop',
  shorts: 'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600&h=400&fit=crop',
  trackpants: 'https://images.unsplash.com/photo-1515586838455-8f8f940d6853?w=600&h=400&fit=crop',
  belts: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600&h=400&fit=crop',
  wallets: 'https://images.unsplash.com/photo-1627123424574-724758594e93?w=600&h=400&fit=crop',
};

export function getProductImage(product) {
  const images = CATEGORY_IMAGES[product.category] || CATEGORY_IMAGES.shirts;
  const idx = parseInt(product.id.replace('p', ''), 10) % images.length;
  return images[idx];
}

export function getCategoryImage(category) {
  return CATEGORY_COVER[category] || CATEGORY_COVER.shirts;
}

export const CATEGORY_LABELS = {
  shirts: 'Shirts',
  trousers: 'Trousers',
  shoes: 'Shoes',
  tshirts: 'T-Shirts',
  jackets: 'Jackets',
  watches: 'Watches',
  bags: 'Bags',
  sunglasses: 'Sunglasses',
  dresses: 'Dresses',
  kurta: 'Kurta',
  ethnic: 'Ethnic',
  shorts: 'Shorts',
  trackpants: 'Track Pants',
  belts: 'Belts',
  wallets: 'Wallets',
};
