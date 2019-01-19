from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('assets/1.jpg').convert('RGBA')

# make blank image for the text
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

# get a font
fnt = ImageFont.truetype('fonts/Architex.ttf', 50)
d = ImageDraw.Draw(txt)

# draw text with half opacity()
# def print_text(username):
#     # hello text
#     d.text((15, 10), "Hello there\nnot_umce", font=fnt, fill=(255, 153, 153, 255))
#     d.text((15, 200), "You've got\nthis.", font=fnt, fill=(255, 153, 153, 255))
#     d.text((500, 310), "With love,\nValkyrie Online.", font=fnt, fill=(255, 153, 153, 255))


d.text((15, 10), "Hello there\nnot_umce", font=fnt, fill=(255, 153, 153, 255))
d.text((15, 200), "You've got\nthis.", font=fnt, fill=(255, 153, 153, 255))
d.text((500, 310), "With love,\nValkyrie Online.", font=fnt, fill=(255, 153, 153, 255))
out = Image.alpha_composite(base, txt)

out.show()