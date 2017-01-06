#!/usr/bin/python
# -*- coding: utf-8 -*-

## contact extracted from salesforce report and formated ready to import in google contacts

import csv
import datetime

# Let’s open our report csv file
    
sourcefile = open('report.csv', 'r')
sourcereader = csv.reader(sourcefile, delimiter=';', quotechar='"')

# Let's open our template google contacts file

exportfilename = 'contacts' + '_' + "-".join(str(datetime.datetime.now())[:-7]) + '.csv'
contactsfile = open(exportfilename, 'w')
contactswriter = csv.writer(contactsfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

contactswriter.writerow(['Name','Given Name','Family Name','Group Membership','E-mail 1 - Type','E-mail 1 - Value','Phone 1 - Type','Phone 1 - Value'])

for row in sourcereader:
    #fix phone numbers that don't start with 0'
    if row[9].startswith('33'):
        row[9] = "0" + row[9][2:]
    elif row[9].startswith('6') or row[9].startswith('7') or row[9].startswith('8') or row[9].startswith('9'):
        row[9] = "0" + row[9]
    stuff = [" ".join([row[1].capitalize(),row[2].capitalize()]),row[1].capitalize(),row[2].capitalize(),'Praticiens','* Work',row[10],'Mobile',row[9],]
    contactswriter.writerow(stuff)


sourcefile.close()
contactsfile.close()
