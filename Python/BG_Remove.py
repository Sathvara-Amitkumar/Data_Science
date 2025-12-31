from PIL import Image
from rembg import remove

remove(Image.open(input(""))).save(input("myBG"))