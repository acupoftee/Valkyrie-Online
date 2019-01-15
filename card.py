from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('love/iu-1.png').convert('RGBA')

# make blank image for the text
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

# get a font
fnt = ImageFont.truetype('fonts/Architex.ttf', 200)
d = ImageDraw.Draw(txt)

# draw text with half opacity()
d.text((30, 10), "Hello there", font=fnt, fill=(255, 153, 153, 255))

out = Image.alpha_composite(base, txt)

out.show()