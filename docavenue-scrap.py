#!/usr/bin/python3
# -*- coding: utf-8 -*-

# objectif : sortir une liste de prats réservables sur pjd

import requests, bs4, csv, datetime

baseurl = 'https://www.docavenue.com'

spes = ['medecins']

departements = ['69',
                '42',
                '38',
                '01',
                '26',
                '43',
                ]


for departement in departements:
    # Créons notre fichier de résultat csv

    resultFileName = 'Docavenue' + '_' + departement +'.csv'
    result = open(resultFileName, 'w')
    resultWriter = csv.writer(result, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Contenu de la première ligne du tableau de résultats
    resultWriter.writerow(['Spécialité','Nom','Adresse', 'Code postal', 'Ville', 'Lien'])

    compteur = 0

    for spe in spes:
        url = baseurl + '/' + spe + '/' + departement

        for numpage in range(1,4):
            url = url + '?page=' + str(numpage)
            print(url)
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            prats = soup.select("div.card-main")
            print(prats)

            for prat in prats:
                nom = prat.parent.p.get_text()
                adresse = prat.parent.find("span", itemprop="streetAddress").get_text()
                adresse = adresse.strip("\n")
                specialty = prat.parent.find("span", itemprop="medicalSpecialty").get_text()
                cp = prat.parent.find("span", itemprop="postalCode").get_text()
                ville = prat.parent.find("span", itemprop="addressLocality").get_text()
                lien = prat.parent.find("a", class_="ps-link-schedule").get('href')
                lien = baseurl + lien
                myRow = [specialty, nom, adresse, cp, ville, lien]
                print(myRow)
                resultWriter.writerow(myRow)
                compteur += 1
            url = baseurl + '/' + spe + '/' + departement


    print('Travail terminé sur', departement, ', {0} prats ont été scrapés.'.format(compteur))
