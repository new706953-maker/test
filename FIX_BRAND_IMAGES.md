# Fix Brand Logos and Banners

## The Problem

The brand logos and banners are not showing because the database has invalid placeholder URLs (using the old `via.placeholder.com` format with `.png` extension which doesn't work).

## The Solution

Run this Python script to update all brand logos and banners with working placeholder URLs:

```bash
cd backend
python update_brand_images.py
```

Or if you use Python 3:

```bash
cd backend
python3 update_brand_images.py
```

## What This Does

The script will:
1. Connect to your MongoDB database
2. Update all 5 brands (BEST, Walkaroo, Action, Brilliant, Chinese) with working `placehold.co` image URLs
3. Each brand will get a unique colored logo and banner
4. Display verification showing the updated URLs

## After Running the Script

You should see output like:
```
✓ Updated best
  Logo: https://placehold.co/200x80/dc2626/white?text=BEST
  Banner: https://placehold.co/1200x300/dc2626/white?text=BEST+Premium+PU+Slippers

✓ Updated walkaroo
  Logo: https://placehold.co/200x80/16a34a/white?text=Walkaroo
  Banner: https://placehold.co/1200x300/16a34a/white?text=Walkaroo+Comfort+Collection
...
```

## Verify It Works

1. Refresh your website
2. You should now see:
   - Brand logos (200x80px colored rectangles with brand names)
   - Brand banners (1200x300px colored rectangles with brand descriptions)
   - Each brand has a different color (red, green, blue, orange, purple)

## Alternative: Manual Database Update

If you can't run the Python script, you can also:

1. Go to your MongoDB Atlas dashboard
2. Navigate to your `daksh_footwear` database
3. Open the `brands` collection
4. For each brand document, update the `logo_url` and `banner_url` fields with the URLs from the script

## Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'pymongo'`

**Solution**: Install pymongo first:
```bash
pip install pymongo
```
or
```bash
pip3 install pymongo
```

**Problem**: Script runs but no brands found

**Solution**: Check that your database name is `daksh_footwear` and the collection name is `brands`
