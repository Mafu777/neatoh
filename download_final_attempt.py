import urllib.request
import urllib.error
import os
import ssl

os.makedirs("images", exist_ok=True)

# Bypass SSL certificate verification (common issue with some servers)
ssl._create_default_https_context = ssl._create_unverified_context

# Try multiple image sources - direct CDN URLs that should work
image_sources = {
    "hero.jpg": [
        "https://images.pexels.com/photos/3938022/pexels-photo-3938022.jpeg?auto=compress&cs=tinysrgb&w=1200&h=600&dpr=1",
        "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/307386301/1800"
    ],
    "service-general.jpg": [
        "https://images.pexels.com/photos/3938379/pexels-photo-3938379.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Gfp-cleaning.jpg/800px-Gfp-cleaning.jpg"
    ],
    "service-construction.jpg": [
        "https://images.pexels.com/photos/3862631/pexels-photo-3862631.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",
        "https://images.unsplash.com/photo-1581092335201-a6c09b1ceeb0?w=800&h=600&fit=crop"
    ],
    "service-rubble.jpg": [
        "https://images.pexels.com/photos/3912997/pexels-photo-3912997.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",
        "https://images.pexels.com/photos/3962286/pexels-photo-3962286.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1"
    ],
    "service-renovation.jpg": [
        "https://images.pexels.com/photos/3769714/pexels-photo-3769714.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",
        "https://images.pexels.com/photos/3852398/pexels-photo-3852398.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1"
    ]
}

print("Attempting to download real images from multiple sources...")

for filename, urls in image_sources.items():
    filepath = os.path.join("images", filename)
    downloaded = False
    
    for url in urls:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Referer': 'https://www.google.com/',
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
            }
            req = urllib.request.Request(url, headers=headers)
            
            print(f"Downloading {filename}...", end=" ", flush=True)
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    data = response.read()
                    f.write(data)
                    print(f"✓ Done ({len(data)} bytes)")
            downloaded = True
            break
        except Exception as e:
            print(f"(trying alternate source...)", end=" ", flush=True)
    
    if not downloaded:
        print(f"✗ Failed - file not updated")

print("\n✅ Download attempt completed!")
