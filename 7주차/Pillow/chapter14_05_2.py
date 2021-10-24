from PIL import Image
img = Image.open('baby.jpg')
img_s = img.resize((500, 500))
img_s.show()
