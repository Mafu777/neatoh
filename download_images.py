import urllib.request
import urllib.error
import os

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# Better image URLs from Unsplash CDN (more reliable)
images_to_download = {
    "hero.jpg": "https://images.unsplash.com/photo-1563207153-f403bf289096?w=1200&h=600&fit=crop",  # Cleaning service
    "service-general.jpg": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=800&h=600&fit=crop",  # Professional cleaning
    "service-construction.jpg": "https://images.unsplash.com/photo-1581091918484-24ad5261a37d?w=800&h=600&fit=crop",  # Construction
    "service-rubble.jpg": "https://images.unsplash.com/photo-1581092160562-40038f73e624?w=800&h=600&fit=crop",  # Debris/waste
    "service-renovation.jpg": "https://images.unsplash.com/photo-1581092161562-40038f73e624?w=800&h=600&fit=crop"  # Renovation
}

print("Downloading real images from Unsplash...")

for filename, url in images_to_download.items():
    filepath = os.path.join("images", filename)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        
        print(f"Downloading {filename}...", end=" ")
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print("✓ Done")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✅ Image download attempt completed!")
