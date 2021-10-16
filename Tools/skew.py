from PIL import Image

img = Image.open("C:\\Users\\Alexis\\Desktop\\python-interfaz\\img1.png")

width, height = img.size
m = -0.5
xshift = abs(m) * width
new_width = width + int(round(xshift))
out = img.transform((new_width, height), Image.AFFINE,
        (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)

img.show()
out.show()


input()