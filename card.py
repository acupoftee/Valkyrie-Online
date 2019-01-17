from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('assets/1.jpg').convert('RGBA')

# make blank image for the text
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

# get a font
fnt = ImageFont.truetype('fonts/Architex.ttf', 70)
d = ImageDraw.Draw(txt)

# draw text with half opacity()
d.text((20, 10), "Hello there", font=fnt, fill=(255, 153, 153, 255))

out = Image.alpha_composite(base, txt)

out.show()