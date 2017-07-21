#!/usr/bin/python3
# -*- coding: utf-8 -*-

## contact extracted from salesforce report and formated ready to import in google contacts

import csv
import datetime
import sys

# Let’s open our report csv file
reports = sys.argv

report = reports[1]
sourcefile = open(report, 'r')

sourcereader = csv.reader(sourcefile, delimiter=';', quotechar='"')

# Let's create our template google contacts file

exportfilename = 'contacts' + '_' + str(datetime.datetime.now())[:-7] + '.csv'
contactsfile = open(exportfilename, 'w')
contactswriter = csv.writer(contactsfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# first line of the contacts csv file
contactswriter.writerow(['Name','Given Name','Family Name','Group Membership','E-mail 1 - Type','E-mail 1 - Value','Phone 1 - Type','Phone 1 - Value','Phone 2 - Type', 'Phone 2 - Value'])

# trick to skip the first line in the source file
firstline = True
counter = 0

def fix_number(phone_number):
    '''fix phone numbers that don't start with 0'''
    if phone_number.startswith('33'):
        phone_number = '0' + phone_number[2:]
    elif phone_number.startswith('6') or phone_number.startswith('7') or phone_number.startswith('8') or phone_number.startswith('9'):
        phone_number = '0' + phone_number
    return phone_number


for row in sourcereader:
    if firstline:
        firstline = False
        continue

    stuff = [" ".join([row[1].title(),row[2].title()]),row[1].title(),row[2].title(),'Praticiens','* Work',row[10],'Work',fix_number(row[8]),'Mobile',fix_number(row[9])]
    contactswriter.writerow(stuff)
    counter += 1

sourcefile.close()
contactsfile.close()
print('Travail terminé, {0} contacts prêts à être importés.'.format(counter))
