from PIL import Image

infile = input("Insert filename:")
horizontal = int(input("horizontal:"))
vertical = int(input("vertical:"))


img = Image.open(infile)
width, height = img.size

chopsizeW, chopsizeH = width // horizontal, height // vertical

# Save Chops of original image
for x0 in range(0, width, chopsizeW):
   for y0 in range(0, height, chopsizeH):
      box = (x0, y0,
             x0+chopsizeW if x0+chopsizeW <  width else  width - 1,
             y0+chopsizeH if y0+chopsizeH < height else height - 1)
      print('%s %s' % (infile, box))
      img.crop(box).save('zchop.%s.x%03d.y%03d.jpg' % (infile.replace('.jpg',''), x0, y0))