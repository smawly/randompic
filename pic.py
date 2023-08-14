from PIL import Image, ImageDraw
import random

def generate_random_image(width, height):
    img = Image.new('RGB', (width, height), color = 'white')
    draw = ImageDraw.Draw(img)
    for i in range(10):
        x1 = random.randint(0,width)
        y1 = random.randint(0,height)
        x2 = random.randint(0,width)
        y2 = random.randint(0,height)
        r,g,b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
        draw.line((x1,y1,x2,y2),fill=(r,g,b),width=3)
    return img

img = generate_random_image(200, 200)
img.show()
