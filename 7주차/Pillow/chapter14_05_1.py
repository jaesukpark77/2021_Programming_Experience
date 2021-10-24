from PIL import Image
img = Image.open('baby.jpg')
img_r = img.rotate(90)
img_r.show()
