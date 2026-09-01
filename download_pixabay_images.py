import urllib.request
import urllib.error
import json
import os

os.makedirs("images", exist_ok=True)

# Pixabay API - free, no authentication required for URL access
# These are direct image URLs from Pixabay (royalty-free)
images_to_download = {
    "hero.jpg": "https://cdn.pixabay.com/photo/2019/02/04/21/54/office-3876373_1280.jpg",  # Professional office
    "service-general.jpg": "https://cdn.pixabay.com/photo/2020/04/18/17/45/cleaning-5062508_1280.jpg",  # Cleaning supplies
    "service-construction.jpg": "https://cdn.pixabay.com/photo/2020/08/22/17/09/building-5508695_1280.jpg",  # Construction
    "service-rubble.jpg": "https://cdn.pixabay.com/photo/2019/06/04/16/19/waste-4253662_1280.jpg",  # Waste/debris
    "service-renovation.jpg": "https://cdn.pixabay.com/photo/2016/11/18/14/56/hammer-1835182_1280.jpg"  # Tools/renovation
}

print("Downloading real images from Pixabay...")

for filename, url in images_to_download.items():
    filepath = os.path.join("images", filename)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        
        print(f"Downloading {filename}...", end=" ")
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print("✓ Done")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✅ Image download completed!")
