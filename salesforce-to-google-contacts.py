#!/usr/bin/python
# -*- coding: utf-8 -*-

## contact extracted from salesforce report and formated ready to import in google contacts

import csv
import datetime

# Let’s open our report csv file
report = input("Quel est le report à traiter ?")
    
sourcefile = open(report, 'r')
sourcereader = csv.reader(sourcefile, delimiter=';', quotechar='"')

# Let's open our template google contacts file

exportfilename = 'contacts' + '_' + str(datetime.datetime.now())[:-7] + '.csv'
contactsfile = open(exportfilename, 'w')
contactswriter = csv.writer(contactsfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

contactswriter.writerow(['Name','Given Name','Family Name','Group Membership','E-mail 1 - Type','E-mail 1 - Value','Phone 1 - Type','Phone 1 - Value','Phone 2 - Type', 'Phone 2 - Value'])

firstline = True
counter = 0

for row in sourcereader:
# skip the first line
    if firstline:
        firstline = False
        continue
    #fix phone numbers that don't start with 0'
    if row[8].startswith('33'):
        row[8] = "0" + row[8][2:]
    elif row[8].startswith('6') or row[8].startswith('7') or row[8].startswith('8') or row[8].startswith('9'):
        row[8] = "0" + row[8]

    if row[9].startswith('33'):
        row[9] = "0" + row[9][2:]
    elif row[9].startswith('6') or row[9].startswith('7') or row[9].startswith('8') or row[9].startswith('9'):
        row[9] = "0" + row[9]

    stuff = [" ".join([row[1].title(),row[2].title()]),row[1].title(),row[2].title(),'Praticiens','* Work',row[10],'Work',row[8],'Mobile',row[9]]
    contactswriter.writerow(stuff)
    counter += 1

sourcefile.close()
contactsfile.close()
print('Travail terminé, {0} contacts prêts à être importés.'.format(counter))
