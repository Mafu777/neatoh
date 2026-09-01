from PIL import Image, ImageDraw, ImageFilter
import os

os.makedirs("images", exist_ok=True)

def add_texture(image, opacity=0.3):
    """Add subtle noise/texture overlay"""
    import random
    pixels = image.load()
    width, height = image.size
    for i in range(width):
        for j in range(height):
            if random.random() > 0.95:
                r, g, b = pixels[i, j][:3]
                noise = random.randint(-20, 20)
                r = max(0, min(255, r + noise))
                g = max(0, min(255, g + noise))
                b = max(0, min(255, b + noise))
                pixels[i, j] = (r, g, b, 255)
    return image

def create_hero_image():
    """Professional office/construction site with warm tones"""
    img = Image.new('RGB', (1200, 600), color=(245, 240, 235))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Gradient background - warm office tones
    for i in range(600):
        ratio = i / 600
        r = int(245 - (40 * ratio))
        g = int(240 - (50 * ratio))
        b = int(235 - (60 * ratio))
        draw.rectangle([(0, i), (1200, i+1)], fill=(r, g, b))
    
    # Large geometric shapes suggesting construction/office
    draw.rectangle([(0, 150), (400, 550)], fill=(120, 120, 110, 80))  # Dark column
    draw.rectangle([(600, 100), (1100, 500)], fill=(200, 150, 80, 60))  # Warm rectangle
    
    # Text/overlay
    try:
        draw.text((100, 250), "Professional Cleaning Services", fill=(50, 50, 50, 200))
    except:
        pass
    
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    return img

def create_general_cleaning():
    """Bright office/floor cleaning aesthetic"""
    img = Image.new('RGB', (800, 600), color=(220, 220, 215))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Gradient from light to slightly darker
    for i in range(600):
        ratio = i / 600
        r = int(220 - (30 * ratio))
        g = int(220 - (35 * ratio))
        b = int(215 - (40 * ratio))
        draw.rectangle([(0, i), (800, i+1)], fill=(r, g, b))
    
    # Geometric patterns suggesting floor tiles and cleanliness
    tile_size = 100
    for x in range(0, 800, tile_size):
        for y in range(0, 600, tile_size):
            if (x + y) % (tile_size * 2) == 0:
                draw.rectangle([(x, y), (x + tile_size, y + tile_size)], 
                              fill=(240, 235, 230, 100), outline=(180, 180, 170, 150))
    
    # Bright accent lines
    draw.rectangle([(50, 50), (750, 100)], fill=(200, 150, 80, 120))
    
    img = img.filter(ImageFilter.GaussianBlur(radius=1.5))
    return img

def create_construction_cleaning():
    """Construction site with industrial colors"""
    img = Image.new('RGB', (800, 600), color=(180, 170, 160))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Gradient - construction site tones
    for i in range(600):
        ratio = i / 600
        r = int(180 - (50 * ratio))
        g = int(170 - (45 * ratio))
        b = int(160 - (40 * ratio))
        draw.rectangle([(0, i), (800, i+1)], fill=(r, g, b))
    
    # Building-like structures
    draw.rectangle([(50, 100), (300, 500)], fill=(120, 120, 110, 80))
    draw.rectangle([(350, 80), (650, 480)], fill=(150, 140, 130, 90))
    draw.rectangle([(700, 120), (800, 450)], fill=(100, 100, 95, 85))
    
    # Accent color (gold/brass like logo)
    draw.rectangle([(0, 0), (800, 30)], fill=(200, 150, 80, 150))
    
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    return img

def create_rubble_removal():
    """Dark industrial/waste removal aesthetic"""
    img = Image.new('RGB', (800, 600), color=(140, 135, 130))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Dark industrial gradient
    for i in range(600):
        ratio = i / 600
        r = int(140 - (40 * ratio))
        g = int(135 - (40 * ratio))
        b = int(130 - (35 * ratio))
        draw.rectangle([(0, i), (800, i+1)], fill=(r, g, b))
    
    # Pile/debris shapes
    draw.ellipse([(50, 300), (250, 550)], fill=(100, 95, 90, 120))
    draw.ellipse([(280, 250), (450, 500)], fill=(120, 115, 110, 110))
    draw.ellipse([(500, 280), (750, 520)], fill=(110, 105, 100, 115))
    
    # Brass accent
    draw.rectangle([(0, 0), (800, 20)], fill=(200, 150, 80, 160))
    draw.rectangle([(0, 580), (800, 600)], fill=(180, 130, 60, 140))
    
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    return img

def create_renovation_support():
    """Active work area with warm industrial tones"""
    img = Image.new('RGB', (800, 600), color=(200, 185, 170))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Warm industrial gradient
    for i in range(600):
        ratio = i / 600
        r = int(200 - (60 * ratio))
        g = int(185 - (50 * ratio))
        b = int(170 - (40 * ratio))
        draw.rectangle([(0, i), (800, i+1)], fill=(r, g, b))
    
    # Work area patterns
    draw.rectangle([(0, 0), (800, 150)], fill=(250, 240, 230, 100))  # Top light area
    draw.rectangle([(0, 150), (800, 600)], fill=(130, 120, 110, 80))  # Work area
    
    # Tool/equipment shapes
    draw.rectangle([(100, 250), (200, 400)], fill=(180, 160, 140, 120))
    draw.rectangle([(300, 200), (400, 450)], fill=(160, 140, 120, 130))
    draw.rectangle([(500, 220), (650, 480)], fill=(170, 150, 130, 125))
    
    # Brass accents
    draw.rectangle([(0, 140), (800, 160)], fill=(200, 150, 80, 140))
    
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    return img

print("Creating professional images...")

images = {
    "hero.jpg": create_hero_image(),
    "service-general.jpg": create_general_cleaning(),
    "service-construction.jpg": create_construction_cleaning(),
    "service-rubble.jpg": create_rubble_removal(),
    "service-renovation.jpg": create_renovation_support()
}

for filename, img in images.items():
    filepath = os.path.join("images", filename)
    img.save(filepath, quality=95)
    print(f"✓ {filename} created")

print("\n✅ All professional images created successfully!")
