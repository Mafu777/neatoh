from PIL import Image, ImageDraw, ImageFilter
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Hero image - construction site with cleaning
hero = Image.new('RGB', (1200, 600), color='#2B332F')
draw = ImageDraw.Draw(hero)

# Add gradient-like effect with rectangles
for i in range(600):
    color_val = int(43 + (i/600) * 40)
    draw.rectangle([(0, i), (1200, i+1)], fill=(color_val, color_val+10, color_val-5))

# Add some industrial texture
for x in range(0, 1200, 100):
    for y in range(0, 600, 100):
        draw.rectangle([(x, y), (x+50, y+50)], outline='#C89B3C', width=1)

hero.save('images/hero.jpg', 'JPEG', quality=90)
print("✓ Hero image created")

# Service 1 - General cleaning (office/interior)
service1 = Image.new('RGB', (800, 600), color='#E1DED2')
draw = ImageDraw.Draw(service1)

# Light interior with floor tiles
for i in range(0, 800, 100):
    for j in range(0, 600, 100):
        if (i + j) % 200 == 0:
            draw.rectangle([(i, j), (i+100, j+100)], fill='#D3D0C3', outline='#C89B3C', width=2)
        else:
            draw.rectangle([(i, j), (i+100, j+100)], fill='#E1DED2', outline='#C89B3C', width=2)

service1.save('images/service-general.jpg', 'JPEG', quality=90)
print("✓ General cleaning image created")

# Service 2 - Construction cleaning
service2 = Image.new('RGB', (800, 600), color='#6E6E62')
draw = ImageDraw.Draw(service2)

# Darker construction site with some details
for i in range(0, 800, 80):
    draw.line([(i, 0), (i, 600)], fill='#8C6A24', width=2)
for i in range(0, 600, 80):
    draw.line([(0, i), (800, i)], fill='#8C6A24', width=2)

# Add some "dusty" look
for i in range(200):
    draw.point((i*4, i*3), fill='#9CA39D')

service2.save('images/service-construction.jpg', 'JPEG', quality=90)
print("✓ Construction cleaning image created")

# Service 3 - Rubble removal
service3 = Image.new('RGB', (800, 600), color='#4A4A42')
draw = ImageDraw.Draw(service3)

# Darker image for rubble
for i in range(20):
    x1, y1 = i*40, i*30
    x2, y2 = x1+150, y1+100
    draw.rectangle([(x1, y1), (x2, y2)], fill='#5A5A52', outline='#C89B3C', width=1)
    draw.rectangle([(x2-150, y1+100), (x2, y1+200)], fill='#6A6A62', outline='#8C6A24', width=1)

service3.save('images/service-rubble.jpg', 'JPEG', quality=90)
print("✓ Rubble removal image created")

# Service 4 - Renovation support
service4 = Image.new('RGB', (800, 600), color='#5A5A52')
draw = ImageDraw.Draw(service4)

# Active work area with tools/materials
for i in range(0, 800, 120):
    for j in range(0, 600, 120):
        if (i//120 + j//120) % 3 == 0:
            draw.rectangle([(i, j), (i+80, j+80)], fill='#C89B3C', outline='#8C6A24', width=2)
        else:
            draw.rectangle([(i, j), (i+80, j+80)], fill='#6E6E62', outline='#9CA39D', width=1)

service4.save('images/service-renovation.jpg', 'JPEG', quality=90)
print("✓ Renovation support image created")

print("\n✅ All images created successfully!")
