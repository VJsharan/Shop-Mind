"""
Seed Firestore with 50 mock retail products.
Run once before starting the app: python seed_firestore.py
"""

import os
from google.cloud import firestore
from dotenv import load_dotenv

load_dotenv()

PRODUCTS = [
    # Formal Shirts
    {"id": "p001", "name": "ArrowFlex Blue Formal Shirt", "category": "shirts", "sub_category": "formal", "color": "blue", "price": 1299, "brand": "Arrow", "occasion": ["interview", "office", "formal"], "sizes": ["S","M","L","XL"], "rating": 4.3, "stock": 45, "description": "Slim fit cotton formal shirt with wrinkle-resistant fabric."},
    {"id": "p002", "name": "Peter England White Formal Shirt", "category": "shirts", "sub_category": "formal", "color": "white", "price": 999, "brand": "Peter England", "occasion": ["interview", "office", "formal"], "sizes": ["S","M","L","XL","XXL"], "rating": 4.5, "stock": 60, "description": "Classic fit formal shirt, ideal for interviews."},
    {"id": "p003", "name": "Van Heusen Navy Slim Shirt", "category": "shirts", "sub_category": "formal", "color": "navy", "price": 1499, "brand": "Van Heusen", "occasion": ["interview", "office"], "sizes": ["M","L","XL"], "rating": 4.4, "stock": 30, "description": "Premium navy slim fit shirt with stretch comfort."},
    {"id": "p004", "name": "Raymond Blue Striped Formal Shirt", "category": "shirts", "sub_category": "formal", "color": "blue", "price": 1799, "brand": "Raymond", "occasion": ["office", "formal", "wedding"], "sizes": ["S","M","L","XL"], "rating": 4.6, "stock": 20, "description": "Fine stripe pattern formal shirt with premium cotton."},
    {"id": "p005", "name": "Zara Casual Blue Shirt", "category": "shirts", "sub_category": "casual", "color": "blue", "price": 2499, "brand": "Zara", "occasion": ["casual", "outing"], "sizes": ["S","M","L"], "rating": 4.2, "stock": 15, "description": "Relaxed fit casual shirt for everyday wear."},

    # Trousers
    {"id": "p006", "name": "Arrow Black Formal Trousers", "category": "trousers", "sub_category": "formal", "color": "black", "price": 1599, "brand": "Arrow", "occasion": ["interview", "office", "formal"], "sizes": ["30","32","34","36"], "rating": 4.4, "stock": 40, "description": "Slim fit formal trousers with flat front design."},
    {"id": "p007", "name": "Peter England Grey Trousers", "category": "trousers", "sub_category": "formal", "color": "grey", "price": 1299, "brand": "Peter England", "occasion": ["office", "interview"], "sizes": ["30","32","34","36","38"], "rating": 4.3, "stock": 35, "description": "Regular fit comfortable formal trousers."},
    {"id": "p008", "name": "Levi's 511 Blue Jeans", "category": "trousers", "sub_category": "jeans", "color": "blue", "price": 2999, "brand": "Levis", "occasion": ["casual", "outing"], "sizes": ["30","32","34","36"], "rating": 4.6, "stock": 50, "description": "Slim fit jeans in mid-blue wash."},
    {"id": "p009", "name": "H&M Chinos Beige", "category": "trousers", "sub_category": "chinos", "color": "beige", "price": 1799, "brand": "H&M", "occasion": ["casual", "smart casual", "college"], "sizes": ["30","32","34"], "rating": 4.1, "stock": 25, "description": "Slim fit chinos for smart casual looks."},
    {"id": "p010", "name": "Park Avenue Navy Formal Trousers", "category": "trousers", "sub_category": "formal", "color": "navy", "price": 1899, "brand": "Park Avenue", "occasion": ["interview", "office", "formal"], "sizes": ["32","34","36"], "rating": 4.5, "stock": 18, "description": "Premium formal trousers with crease-resistant fabric."},

    # Shoes
    {"id": "p011", "name": "Hush Puppies Black Oxford Shoes", "category": "shoes", "sub_category": "formal", "color": "black", "price": 3499, "brand": "Hush Puppies", "occasion": ["interview", "office", "formal"], "sizes": ["7","8","9","10","11"], "rating": 4.5, "stock": 22, "description": "Classic leather oxford shoes for formal occasions."},
    {"id": "p012", "name": "Red Tape Brown Derby Shoes", "category": "shoes", "sub_category": "formal", "color": "brown", "price": 2799, "brand": "Red Tape", "occasion": ["office", "formal", "smart casual"], "sizes": ["7","8","9","10"], "rating": 4.3, "stock": 18, "description": "Genuine leather derby shoes with cushioned insole."},
    {"id": "p013", "name": "Nike Air Max 270 White", "category": "shoes", "sub_category": "sneakers", "color": "white", "price": 9999, "brand": "Nike", "occasion": ["casual", "sports", "gym"], "sizes": ["7","8","9","10","11"], "rating": 4.7, "stock": 12, "description": "Lightweight air-cushioned sneakers."},
    {"id": "p014", "name": "Woodland Brown Casual Shoes", "category": "shoes", "sub_category": "casual", "color": "brown", "price": 2499, "brand": "Woodland", "occasion": ["casual", "college", "outing"], "sizes": ["7","8","9","10","11"], "rating": 4.4, "stock": 30, "description": "Durable leather casual shoes for everyday wear."},
    {"id": "p015", "name": "Adidas Stan Smith Green", "category": "shoes", "sub_category": "sneakers", "color": "white", "price": 7999, "brand": "Adidas", "occasion": ["casual", "outing"], "sizes": ["7","8","9","10"], "rating": 4.6, "stock": 10, "description": "Iconic low-top sneakers with green heel tab."},

    # T-Shirts
    {"id": "p016", "name": "H&M Basic White T-Shirt", "category": "tshirts", "sub_category": "basic", "color": "white", "price": 599, "brand": "H&M", "occasion": ["casual", "home", "gym"], "sizes": ["S","M","L","XL"], "rating": 4.0, "stock": 100, "description": "100% cotton basic crew neck t-shirt."},
    {"id": "p017", "name": "Bewakoof Black Graphic Tee", "category": "tshirts", "sub_category": "graphic", "color": "black", "price": 449, "brand": "Bewakoof", "occasion": ["casual", "college", "outing"], "sizes": ["S","M","L","XL","XXL"], "rating": 4.1, "stock": 75, "description": "Quirky graphic print t-shirt in soft cotton."},
    {"id": "p018", "name": "Uniqlo Navy Polo T-Shirt", "category": "tshirts", "sub_category": "polo", "color": "navy", "price": 1499, "brand": "Uniqlo", "occasion": ["smart casual", "office", "college"], "sizes": ["S","M","L","XL"], "rating": 4.5, "stock": 40, "description": "Classic pique polo shirt in navy blue."},
    {"id": "p019", "name": "Zara White Polo", "category": "tshirts", "sub_category": "polo", "color": "white", "price": 1999, "brand": "Zara", "occasion": ["smart casual", "outing"], "sizes": ["S","M","L"], "rating": 4.3, "stock": 22, "description": "Slim fit polo shirt with contrast collar."},
    {"id": "p020", "name": "Puma Red Sports Tee", "category": "tshirts", "sub_category": "sports", "color": "red", "price": 899, "brand": "Puma", "occasion": ["gym", "sports", "casual"], "sizes": ["S","M","L","XL"], "rating": 4.2, "stock": 55, "description": "Moisture-wicking sports t-shirt with DryCell technology."},

    # Jackets
    {"id": "p021", "name": "H&M Black Bomber Jacket", "category": "jackets", "sub_category": "bomber", "color": "black", "price": 3499, "brand": "H&M", "occasion": ["casual", "outing", "college"], "sizes": ["S","M","L","XL"], "rating": 4.4, "stock": 20, "description": "Classic bomber jacket with ribbed cuffs."},
    {"id": "p022", "name": "Mufti Brown Leather Jacket", "category": "jackets", "sub_category": "leather", "color": "brown", "price": 5999, "brand": "Mufti", "occasion": ["casual", "outing", "party"], "sizes": ["S","M","L","XL"], "rating": 4.5, "stock": 10, "description": "Faux leather biker jacket with zip detailing."},
    {"id": "p023", "name": "Columbia Blue Windbreaker", "category": "jackets", "sub_category": "windbreaker", "color": "blue", "price": 4499, "brand": "Columbia", "occasion": ["outdoor", "travel", "casual"], "sizes": ["S","M","L","XL"], "rating": 4.6, "stock": 15, "description": "Lightweight waterproof windbreaker for outdoor activities."},
    {"id": "p024", "name": "Raymond Navy Blazer", "category": "jackets", "sub_category": "blazer", "color": "navy", "price": 6999, "brand": "Raymond", "occasion": ["formal", "interview", "wedding", "office"], "sizes": ["38","40","42","44"], "rating": 4.7, "stock": 12, "description": "Single-breasted formal blazer in premium fabric."},
    {"id": "p025", "name": "Allen Solly Grey Blazer", "category": "jackets", "sub_category": "blazer", "color": "grey", "price": 5499, "brand": "Allen Solly", "occasion": ["office", "formal", "smart casual"], "sizes": ["38","40","42","44"], "rating": 4.4, "stock": 8, "description": "Smart grey blazer for business casual occasions."},

    # Dresses (Women)
    {"id": "p026", "name": "Fabindia Floral Kurta Blue", "category": "kurta", "sub_category": "casual", "color": "blue", "price": 1799, "brand": "Fabindia", "occasion": ["casual", "festive", "college"], "sizes": ["XS","S","M","L","XL"], "rating": 4.5, "stock": 35, "description": "Block print cotton kurta with floral motif."},
    {"id": "p027", "name": "W Black Straight Kurta", "category": "kurta", "sub_category": "formal", "color": "black", "price": 1499, "brand": "W", "occasion": ["office", "formal", "college"], "sizes": ["XS","S","M","L","XL"], "rating": 4.3, "stock": 28, "description": "Solid straight-fit kurta for professional settings."},
    {"id": "p028", "name": "Zara Red Midi Dress", "category": "dresses", "sub_category": "midi", "color": "red", "price": 3999, "brand": "Zara", "occasion": ["party", "date", "outing"], "sizes": ["XS","S","M","L"], "rating": 4.4, "stock": 14, "description": "A-line midi dress in vibrant red."},
    {"id": "p029", "name": "H&M White Linen Dress", "category": "dresses", "sub_category": "casual", "color": "white", "price": 2499, "brand": "H&M", "occasion": ["casual", "outing", "beach"], "sizes": ["XS","S","M","L"], "rating": 4.2, "stock": 20, "description": "Relaxed fit linen dress for summer."},
    {"id": "p030", "name": "Biba Navy Anarkali", "category": "dresses", "sub_category": "ethnic", "color": "navy", "price": 2999, "brand": "Biba", "occasion": ["festive", "wedding", "party"], "sizes": ["XS","S","M","L","XL"], "rating": 4.6, "stock": 16, "description": "Embroidered anarkali with flared silhouette."},

    # Watches
    {"id": "p031", "name": "Fastrack Black Sports Watch", "category": "watches", "sub_category": "sports", "color": "black", "price": 1999, "brand": "Fastrack", "occasion": ["casual", "sports", "college"], "sizes": ["one size"], "rating": 4.2, "stock": 50, "description": "Water-resistant digital sports watch."},
    {"id": "p032", "name": "Titan Edge Silver Watch", "category": "watches", "sub_category": "formal", "color": "silver", "price": 6999, "brand": "Titan", "occasion": ["formal", "office", "interview"], "sizes": ["one size"], "rating": 4.7, "stock": 18, "description": "Ultra-slim formal watch with sapphire glass."},
    {"id": "p033", "name": "Casio G-Shock Black", "category": "watches", "sub_category": "sports", "color": "black", "price": 4999, "brand": "Casio", "occasion": ["sports", "outdoor", "casual"], "sizes": ["one size"], "rating": 4.6, "stock": 25, "description": "Shock-resistant G-Shock with 200m water resistance."},
    {"id": "p034", "name": "Fossil Brown Leather Watch", "category": "watches", "sub_category": "casual", "color": "brown", "price": 8999, "brand": "Fossil", "occasion": ["smart casual", "outing", "date"], "sizes": ["one size"], "rating": 4.5, "stock": 12, "description": "Analog watch with genuine leather strap."},
    {"id": "p035", "name": "Noise ColorFit Pro 4 Black", "category": "watches", "sub_category": "smartwatch", "color": "black", "price": 3499, "brand": "Noise", "occasion": ["casual", "gym", "sports"], "sizes": ["one size"], "rating": 4.3, "stock": 40, "description": "Smartwatch with health tracking and AMOLED display."},

    # Bags
    {"id": "p036", "name": "Wildcraft Grey Backpack", "category": "bags", "sub_category": "backpack", "color": "grey", "price": 1799, "brand": "Wildcraft", "occasion": ["college", "travel", "casual"], "sizes": ["one size"], "rating": 4.4, "stock": 35, "description": "30L backpack with laptop compartment."},
    {"id": "p037", "name": "Samsonite Black Laptop Bag", "category": "bags", "sub_category": "laptop bag", "color": "black", "price": 3499, "brand": "Samsonite", "occasion": ["office", "travel", "college"], "sizes": ["one size"], "rating": 4.6, "stock": 20, "description": "15.6 inch laptop bag with TSA-approved locks."},
    {"id": "p038", "name": "Hidesign Brown Leather Bag", "category": "bags", "sub_category": "shoulder bag", "color": "brown", "price": 4999, "brand": "Hidesign", "occasion": ["office", "formal", "outing"], "sizes": ["one size"], "rating": 4.5, "stock": 12, "description": "Full-grain leather shoulder bag with brass hardware."},
    {"id": "p039", "name": "Lavie Pink Tote Bag", "category": "bags", "sub_category": "tote", "color": "pink", "price": 1499, "brand": "Lavie", "occasion": ["casual", "shopping", "outing"], "sizes": ["one size"], "rating": 4.1, "stock": 30, "description": "Spacious tote bag with multiple compartments."},
    {"id": "p040", "name": "F Gear Navy Duffel Bag", "category": "bags", "sub_category": "duffel", "color": "navy", "price": 2299, "brand": "F Gear", "occasion": ["gym", "travel", "sports"], "sizes": ["one size"], "rating": 4.3, "stock": 25, "description": "45L duffel with shoe compartment."},

    # Sunglasses
    {"id": "p041", "name": "Ray-Ban Aviator Gold", "category": "sunglasses", "sub_category": "aviator", "color": "gold", "price": 7999, "brand": "Ray-Ban", "occasion": ["casual", "driving", "outing"], "sizes": ["one size"], "rating": 4.8, "stock": 10, "description": "Classic gold frame aviator with green lenses."},
    {"id": "p042", "name": "Fastrack Blue Wayfarer", "category": "sunglasses", "sub_category": "wayfarer", "color": "blue", "price": 1299, "brand": "Fastrack", "occasion": ["casual", "college", "outing"], "sizes": ["one size"], "rating": 4.2, "stock": 40, "description": "UV400 protected wayfarer sunglasses."},
    {"id": "p043", "name": "Oakley Black Sports Sunglasses", "category": "sunglasses", "sub_category": "sports", "color": "black", "price": 9999, "brand": "Oakley", "occasion": ["sports", "cycling", "outdoor"], "sizes": ["one size"], "rating": 4.7, "stock": 8, "description": "Polarized sports wrap-around sunglasses."},

    # Ethnic Wear
    {"id": "p044", "name": "Manyavar White Kurta Pajama", "category": "ethnic", "sub_category": "kurta set", "color": "white", "price": 3999, "brand": "Manyavar", "occasion": ["wedding", "festive", "puja"], "sizes": ["S","M","L","XL","XXL"], "rating": 4.6, "stock": 18, "description": "Cotton silk kurta with matching pajama."},
    {"id": "p045", "name": "Manyavar Navy Sherwani", "category": "ethnic", "sub_category": "sherwani", "color": "navy", "price": 12999, "brand": "Manyavar", "occasion": ["wedding", "sangeet", "reception"], "sizes": ["38","40","42","44"], "rating": 4.7, "stock": 6, "description": "Embroidered sherwani with churidar."},

    # Sportswear
    {"id": "p046", "name": "Nike Dri-FIT Black Shorts", "category": "shorts", "sub_category": "sports", "color": "black", "price": 1499, "brand": "Nike", "occasion": ["gym", "sports", "casual"], "sizes": ["S","M","L","XL"], "rating": 4.5, "stock": 45, "description": "Lightweight Dri-FIT training shorts."},
    {"id": "p047", "name": "Adidas Blue Track Pants", "category": "trackpants", "sub_category": "sports", "color": "blue", "price": 1999, "brand": "Adidas", "occasion": ["gym", "sports", "casual"], "sizes": ["S","M","L","XL","XXL"], "rating": 4.4, "stock": 38, "description": "3-Stripe track pants with tapered fit."},
    {"id": "p048", "name": "Puma White Sports Shoes", "category": "shoes", "sub_category": "sports", "color": "white", "price": 3999, "brand": "Puma", "occasion": ["gym", "sports", "casual"], "sizes": ["7","8","9","10","11"], "rating": 4.3, "stock": 22, "description": "Lightweight running shoes with EVA midsole."},

    # Accessories
    {"id": "p049", "name": "Peter England Black Leather Belt", "category": "belts", "sub_category": "formal", "color": "black", "price": 799, "brand": "Peter England", "occasion": ["formal", "office", "interview"], "sizes": ["32","34","36","38","40"], "rating": 4.3, "stock": 60, "description": "Genuine leather formal belt with pin buckle."},
    {"id": "p050", "name": "Tommy Hilfiger Black Wallet", "category": "wallets", "sub_category": "bifold", "color": "black", "price": 2499, "brand": "Tommy Hilfiger", "occasion": ["casual", "formal", "everyday"], "sizes": ["one size"], "rating": 4.5, "stock": 30, "description": "Slim bifold wallet in premium leather."},
]


def seed():
    db = firestore.Client(project=os.getenv("GCP_PROJECT_ID"), database="newdb")
    collection = db.collection("products")

    print(f"Seeding {len(PRODUCTS)} products to Firestore...")
    batch = db.batch()

    for i, product in enumerate(PRODUCTS):
        doc_ref = collection.document(product["id"])
        batch.set(doc_ref, product)

        # Commit in batches of 25 (Firestore limit is 500, but keep it safe)
        if (i + 1) % 25 == 0:
            batch.commit()
            batch = db.batch()
            print(f"  Committed {i + 1} products...")

    batch.commit()
    print(f"✅ Seeding complete. {len(PRODUCTS)} products in Firestore.")


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    seed()
