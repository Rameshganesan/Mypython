import sys
from PIL import Image, ImageFilter

size = (128,128)
myimage = Image.open("C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg")

if Image.isImageType(myimage):
    print("Yes Image")
else:
    print("Not an Image")

list1 = ['BHE','BOW','FHB']


myimage.load()
myimage.show()
blurred = myimage.filter(ImageFilter.BLUR)
blurred.thumbnail(size)
blurred.show()

sys.exit()





