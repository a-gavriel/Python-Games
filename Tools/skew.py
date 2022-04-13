from PIL import Image
import numpy as np




def main():
  #img = Image.open("C:\\Users\\Alexis\\Desktop\\python-interfaz\\img1.png")
  w, h = 512, 512
  data = np.zeros((h, w, 3), dtype=np.uint8)
  data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
  img = Image.fromarray(data, 'RGB')
  #img.save('my.png')
  img.show()

  width, height = img.size
  m = 1.2
  xshift = abs(m) * width//3*2
  new_width = width + int(round(xshift))
  out = img.transform((new_width, height), Image.AFFINE,
    (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)

  out.show()
  input()


main()