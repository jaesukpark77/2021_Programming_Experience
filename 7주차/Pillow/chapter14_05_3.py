from PIL import Image
img = Image.open('baby.jpg')
img_opp = img.transpose(Image.FLIP_LEFT_RIGHT)
img_opp.show()
