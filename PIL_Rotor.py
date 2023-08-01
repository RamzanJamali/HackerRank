import glob
from PIL import Image

images = []
for f in glob.iglob("E://Python/imagess/*"):
    images.append(Image.open(f))

#im = Image.open("rotor_1.jpg")
for i,im in enumerate(images):
    im.rotate(180).resize((640,480)).save("im_{i}.jpg".format(i=i))