# Objectif : redimensionner en masse des images dans un dossier, avant utilisation pour blog ou partage par email par exemple
# TODO : fix si fichier non image présent dans le dossier (genre .directory), fait mais hard codé sur terminaison fichier image en "G" ou "g"

from PIL import Image
from os import listdir
from os.path import isfile, join

mypath = input("Dans quel dossier sont les images ? ")
imageFiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]
target = int(input("Dimension maximum voulue (ex 1000) : "))

for im in imageFiles :
    im1 = Image.open(join(mypath,im))
    originalWidth, originalHeight = im1.size
    ratio = originalWidth / originalHeight
    if ratio > 1 :
        width = target
        height = int(width / ratio)
    else :
        height = target
        width = int(height * ratio)

    im2 = im1.resize((width, height), Image.ANTIALIAS) # linear interpolation in a 2x2 environment
    im2.save(join(mypath, "".join([str(width),"x",str(height),"_",im])))
    print (im, "redimensionnée…")
print ("Travail terminé !", len(imageFiles), "images redimensionnées.")
