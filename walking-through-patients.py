#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Script used to go through folders in a directory, move files one folder up, 
## and then delete the folders they were in
## used to clean up the mess my camera does.

import shutil
import csv
import datetime

from os import listdir
from os.path import isfile, isdir, join

mypath = input("Where are the files to read\n")

exportfilename = 'AA - patients' + '_' + str(datetime.datetime.now())[:-7] + '.csv'
contactsfile = open(exportfilename, 'w')
contactswriter = csv.writer(contactsfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# first line of the contacts csv file
contactswriter.writerow(['Nom','Prénom','E-mail', 'Phone 1','adresse'])
folders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
firstline = True
counter = 0

for folder in folders:
    onlyfiles = [f for f in listdir(join(mypath, folder)) if isfile(join(mypath, folder, f)) and not f.endswith("ini")]
    for f in onlyfiles:
        sourcefile = open(join(mypath, folder, f), 'r', encoding='latin-1')
        stuff = sourcefile.read().splitlines()[0:4444]
        contactswriter.writerow(stuff)
        counter += 1
        sourcefile.close()

contactsfile.close()
print('Travail terminé, {0} contacts prêts à être importés.'.format(counter))
