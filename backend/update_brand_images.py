from pymongo import MongoClient
from datetime import datetime

MONGO_URI = "mongodb+srv://Daksh:Shishamt7894@cluster0.avgzcuo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)
db = client['daksh_footwear']
brands_collection = db['brands']

print("Updating brand logos and banners...")
print("=" * 80)

brands_to_update = [
    {
        'slug': 'best',
        'logo_url': 'https://placehold.co/200x80/dc2626/white?text=BEST',
        'banner_url': 'https://placehold.co/1200x300/dc2626/white?text=BEST+Premium+PU+Slippers'
    },
    {
        'slug': 'walkaroo',
        'logo_url': 'https://placehold.co/200x80/16a34a/white?text=Walkaroo',
        'banner_url': 'https://placehold.co/1200x300/16a34a/white?text=Walkaroo+Comfort+Collection'
    },
    {
        'slug': 'action',
        'logo_url': 'https://placehold.co/200x80/2563eb/white?text=Action',
        'banner_url': 'https://placehold.co/1200x300/2563eb/white?text=Action+Sports+and+School+Footwear'
    },
    {
        'slug': 'brilliant',
        'logo_url': 'https://placehold.co/200x80/ea580c/white?text=Brilliant',
        'banner_url': 'https://placehold.co/1200x300/ea580c/white?text=Brilliant+Quality+Footwear'
    },
    {
        'slug': 'chinese',
        'logo_url': 'https://placehold.co/200x80/9333ea/white?text=Chinese',
        'banner_url': 'https://placehold.co/1200x300/9333ea/white?text=Chinese+Affordable+Footwear'
    }
]

for brand_update in brands_to_update:
    result = brands_collection.update_one(
        {'slug': brand_update['slug']},
        {
            '$set': {
                'logo_url': brand_update['logo_url'],
                'banner_url': brand_update['banner_url'],
                'updated_at': datetime.utcnow()
            }
        }
    )
    if result.matched_count > 0:
        print(f"✓ Updated {brand_update['slug']}")
        print(f"  Logo: {brand_update['logo_url']}")
        print(f"  Banner: {brand_update['banner_url']}")
    else:
        print(f"✗ Brand '{brand_update['slug']}' not found in database")
    print()

print("=" * 80)
print("Update complete!")
print("\nVerifying updates...")
print("=" * 80)

brands = list(brands_collection.find())
for brand in brands:
    print(f"\nBrand: {brand['name']}")
    print(f"  Logo URL: {brand.get('logo_url', 'NOT SET')}")
    print(f"  Banner URL: {brand.get('banner_url', 'NOT SET')}")

print("\n" + "=" * 80)
print("Done! Restart your Flask backend server to see the changes.")
