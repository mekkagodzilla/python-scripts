#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Objectif : redimensionner en masse des images dans un dossier, avant utilisation pour blog ou partage par email par exemple
# TODO : fix si fichier non image présent dans le dossier (genre .directory), fait mais hard codé sur terminaison fichier image en "G" ou "g"

from PIL import Image
from os import listdir, makedirs
from os.path import isfile, join, exists

mypath = input("Where are the images?\n")
imageFiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]
target = int(input("Maximum target length or width (ex 1000): "))

# create resized folder

resized = join(mypath, "resized")

if not exists(resized):
    makedirs(resized)

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
    im2.save(join(resized, "".join([str(width),"x",str(height),"_",im])))
    print (im, "resized…")
print ("Job done!", len(imageFiles), "images resized!")
