import urllib.request
import urllib.error
import os
import ssl

os.makedirs("images", exist_ok=True)

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Proper cleaning and construction themed images from Pexels
image_sources = {
    "hero.jpg": [
        "https://images.pexels.com/photos/3938379/pexels-photo-3938379.jpeg",  # Professional cleaner in uniform
        "https://images.pexels.com/photos/3849586/pexels-photo-3849586.jpeg",  # Woman cleaning office
        "https://images.pexels.com/photos/3938427/pexels-photo-3938427.jpeg"   # Cleaning professional
    ],
    "service-general.jpg": [
        "https://images.pexels.com/photos/3807517/pexels-photo-3807517.jpeg",  # Professional cleaning service
        "https://images.pexels.com/photos/3938379/pexels-photo-3938379.jpeg",  # Cleaner with supplies
        "https://images.pexels.com/photos/3849586/pexels-photo-3849586.jpeg"   # Office cleaning
    ],
    "service-construction.jpg": [
        "https://images.pexels.com/photos/3862631/pexels-photo-3862631.jpeg",  # Construction site cleanup
        "https://images.pexels.com/photos/3935702/pexels-photo-3935702.jpeg",  # Construction workers
        "https://images.pexels.com/photos/3769714/pexels-photo-3769714.jpeg"   # Construction cleanup
    ],
    "service-rubble.jpg": [
        "https://images.pexels.com/photos/3962286/pexels-photo-3962286.jpeg",  # Debris pile
        "https://images.pexels.com/photos/3912997/pexels-photo-3912997.jpeg",  # Waste removal
        "https://images.pexels.com/photos/3938356/pexels-photo-3938356.jpeg"   # Rubble cleanup
    ],
    "service-renovation.jpg": [
        "https://images.pexels.com/photos/3852398/pexels-photo-3852398.jpeg",  # Renovation tools and work
        "https://images.pexels.com/photos/3910071/pexels-photo-3910071.jpeg",  # Construction renovation
        "https://images.pexels.com/photos/87651/wall-tools-work-bench-tools-87651.jpeg"  # Tools on workbench
    ]
}

print("Downloading proper cleaning and construction images...")

for filename, urls in image_sources.items():
    filepath = os.path.join("images", filename)
    downloaded = False
    
    for url in urls:
        try:
            # Add proper headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Referer': 'https://www.pexels.com/',
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
            }
            req = urllib.request.Request(url, headers=headers)
            
            print(f"Downloading {filename}...", end=" ", flush=True)
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    data = response.read()
                    if len(data) > 10000:  # Verify we got actual image data
                        f.write(data)
                        print(f"✓ Done ({len(data)} bytes)")
                        downloaded = True
                        break
                    else:
                        print(f"(file too small, trying next...)", end=" ", flush=True)
        except Exception as e:
            print(f"(trying next source...)", end=" ", flush=True)
    
    if not downloaded:
        print(f"✗ Failed to download")

print("\n✅ Image replacement completed!")
