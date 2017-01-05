## Script used to go through folders in a directory, move files one folder up, 
## and then delete the folders they were in
## used to clean up the mess my camera does.

import shutil
from os import listdir
from os.path import isfile, isdir, join

mypath = input("Dans quel dossier sont les fichiers à remonter ? ")

folders = [f for f in listdir(mypath) if isdir(join(mypath, f))]

for folder in folders:
    onlyfiles = [f for f in listdir(join(mypath, folder)) if isfile(join(mypath, folder, f))]
    for f in onlyfiles:
        shutil.move(join(mypath, folder, f), join(mypath, f))
    shutil.rmtree(join(mypath, folder))
        
      
