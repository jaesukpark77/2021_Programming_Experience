from PIL import Image
img = Image.open('baby.jpg')
print(img.mode)

r,g,b = img.split()
GRB_img = Image.merge('RGB', (g,r,b))
GRB_img.show()
RBG_img = Image.merge('RGB', (r,b,g))
RBG_img.show()
