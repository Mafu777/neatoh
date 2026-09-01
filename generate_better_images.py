from PIL import Image, ImageDraw, ImageFilter
import random
import os

os.makedirs('images', exist_ok=True)

# Hero image - modern construction site with cleaning
hero = Image.new('RGB', (1200, 600), color='#1a1a1a')
draw = ImageDraw.Draw(hero)

# Create a gradient background
for i in range(600):
    r = int(26 + (i/600) * 60)
    g = int(26 + (i/600) * 40)
    b = int(26 + (i/600) * 20)
    draw.rectangle([(0, i), (1200, i+1)], fill=(r, g, b))

# Add modern construction elements - metal and concrete
draw.rectangle([(0, 0), (1200, 150)], fill='#3a3a3a')  # Metal framework
draw.rectangle([(200, 200), (1000, 500)], fill='#5a5a5a', outline='#C89B3C', width=3)  # Building structure

# Add some accent details
for x in range(200, 1000, 150):
    draw.line([(x, 200), (x, 500)], fill='#C89B3C', width=2)

draw.text((100, 250), "Construction Site - Ready for Clean", fill='#C89B3C')
hero.save('images/hero.jpg', 'JPEG', quality=85)
print("✓ Hero image created")

# Service 1 - General Cleaning (bright office)
service1 = Image.new('RGB', (800, 600), color='#f5f5f5')
draw = ImageDraw.Draw(service1)

# Gradient for office feel
for i in range(600):
    shade = int(245 - (i/600) * 30)
    draw.rectangle([(0, i), (800, i+1)], fill=(shade, shade, shade-5))

# Add office floor pattern
for x in range(0, 800, 100):
    for y in range(0, 600, 100):
        draw.rectangle([(x, y), (x+100, y+100)], outline='#dddddd', width=1)

# Add some office furniture representation
draw.rectangle([(100, 100), (300, 250)], fill='#c0c0c0', outline='#808080', width=2)
draw.rectangle([(400, 150), (700, 300)], fill='#d3d3d3', outline='#808080', width=2)

draw.text((150, 400), "General Cleaning", fill='#333333')
service1.save('images/service-general.jpg', 'JPEG', quality=85)
print("✓ General cleaning image created")

# Service 2 - Construction Cleaning
service2 = Image.new('RGB', (800, 600), color='#8a8a7e')
draw = ImageDraw.Draw(service2)

# Dusty construction site feel
for i in range(600):
    shade = int(138 + (i/600) * 40)
    draw.rectangle([(0, i), (800, i+1)], fill=(shade, shade-5, shade-10))

# Add construction elements
draw.rectangle([(50, 100), (400, 450)], fill='#a0a090', outline='#C89B3C', width=2)
draw.rectangle([(450, 150), (750, 400)], fill='#989888', outline='#C89B3C', width=2)

# Add some texture/dust effect
for _ in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    draw.point((x, y), fill='#b0a090')

draw.text((200, 480), "Construction Site Clean", fill='#E8D5B7')
service2.save('images/service-construction.jpg', 'JPEG', quality=85)
print("✓ Construction cleaning image created")

# Service 3 - Rubble Removal
service3 = Image.new('RGB', (800, 600), color='#5a5a52')
draw = ImageDraw.Draw(service3)

# Dark rubble/waste area
for i in range(600):
    shade = int(90 - (i/600) * 30)
    draw.rectangle([(0, i), (800, i+1)], fill=(shade, shade-5, shade-10))

# Add rubble/waste piles
draw.polygon([(50, 400), (200, 200), (350, 400)], fill='#7a7a72')
draw.polygon([(400, 450), (600, 180), (750, 450)], fill='#6a6a62')

# Add some waste material representation
for _ in range(150):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    draw.point((x, y), fill='#8a8a7a')

draw.text((250, 500), "Rubble Removal", fill='#C89B3C')
service3.save('images/service-rubble.jpg', 'JPEG', quality=85)
print("✓ Rubble removal image created")

# Service 4 - Renovation Support
service4 = Image.new('RGB', (800, 600), color='#6a6a5a')
draw = ImageDraw.Draw(service4)

# Active work area
for i in range(600):
    shade = int(106 - (i/600) * 40)
    draw.rectangle([(0, i), (800, i+1)], fill=(shade, shade, shade-10))

# Add work in progress elements
draw.rectangle([(50, 50), (350, 300)], fill='#8a8a7a', outline='#C89B3C', width=3)
draw.rectangle([(400, 100), (750, 350)], fill='#9a9a8a', outline='#C89B3C', width=3)

# Add some tools/materials representation
draw.ellipse([(100, 350), (200, 450)], fill='#C89B3C')
draw.ellipse([(450, 380), (550, 480)], fill='#C89B3C')

draw.text((200, 500), "Renovation Support", fill='#E8D5B7')
service4.save('images/service-renovation.jpg', 'JPEG', quality=85)
print("✓ Renovation support image created")

print("\n✅ All professional images created successfully!")
