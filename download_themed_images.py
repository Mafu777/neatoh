import urllib.request
import urllib.error
import os
import ssl

os.makedirs("images", exist_ok=True)

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Better images that are actually related to cleaning, construction, and renovation
image_sources = {
    "hero.jpg": [
        "https://images.pexels.com/photos/3584622/pexels-photo-3584622.jpeg?auto=compress&cs=tinysrgb&w=1200&h=600&dpr=1",  # Handover/inspection
        "https://images.pexels.com/photos/5632399/pexels-photo-5632399.jpeg?auto=compress&cs=tinysrgb&w=1200&h=600&dpr=1",  # Office inspecting
        "https://images.pexels.com/photos/3407857/pexels-photo-3407857.jpeg?auto=compress&cs=tinysrgb&w=1200&h=600&dpr=1"   # Site inspection
    ],
    "service-general.jpg": [
        "https://images.pexels.com/photos/3807517/pexels-photo-3807517.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Professional cleaning
        "https://images.pexels.com/photos/3938379/pexels-photo-3938379.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Cleaning service
        "https://images.pexels.com/photos/3849586/pexels-photo-3849586.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1"   # Woman cleaning
    ],
    "service-construction.jpg": [
        "https://images.pexels.com/photos/3862631/pexels-photo-3862631.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Construction site
        "https://images.pexels.com/photos/3935702/pexels-photo-3935702.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Construction cleanup
        "https://images.pexels.com/photos/3769714/pexels-photo-3769714.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1"   # Construction work
    ],
    "service-rubble.jpg": [
        "https://images.pexels.com/photos/3962286/pexels-photo-3962286.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Rubble/debris
        "https://images.pexels.com/photos/3912997/pexels-photo-3912997.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Waste removal
        "https://images.pexels.com/photos/5632399/pexels-photo-5632399.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1"   # Cleanup work
    ],
    "service-renovation.jpg": [
        "https://images.pexels.com/photos/3852398/pexels-photo-3852398.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Renovation/tools
        "https://images.pexels.com/photos/3910071/pexels-photo-3910071.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1",  # Construction work
        "https://images.pexels.com/photos/87651/wall-tools-work-bench-tools-87651.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=1"  # Tools/work
    ]
}

print("Downloading cleaning/construction themed images from Pexels...")

for filename, urls in image_sources.items():
    filepath = os.path.join("images", filename)
    downloaded = False
    
    for url in urls:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Referer': 'https://www.pexels.com/',
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
            print(f"(trying alternate...)", end=" ", flush=True)
    
    if not downloaded:
        print(f"✗ Failed")

print("\n✅ Image update completed!")
