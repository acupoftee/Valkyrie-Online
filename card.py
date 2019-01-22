from PIL import Image, ImageDraw, ImageFont
import random

# get an image
image_number = random.randint(1, 24)
if image_number == 2 or image_number == 12 or image_number == 14:
    image_number += 1
base = Image.open('assets/' + str(image_number) + '.jpg').convert('RGBA')

# make blank image for the text
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

# get a font
fnt = ImageFont.truetype('fonts/Architex.ttf', 50)
d = ImageDraw.Draw(txt)

def print_text(greeting, username, response):
    # hello text
    d.text((15, 10), greeting+"\n"+username, font=fnt, fill=(255, 153, 153, 255))
    d.text((15, 200), response, font=fnt, fill=(255, 153, 153, 255))
    d.text((600, 230), "With love,\nValkyrie\nOnline.", font=fnt, fill=(255, 153, 153, 255))


print_text("Hello there", "not_umce", "You've got\nthis.")
out = Image.alpha_composite(base, txt)

# share output and save into output
out.show()