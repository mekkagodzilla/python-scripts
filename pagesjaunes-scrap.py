#!/usr/bin/python3
# -*- coding: utf-8 -*-

# premier script pour manipuler du contenu html avec beautifulsoup.
# objectif : sortir une liste de prats réservables sur pjd

import requests, bs4, csv, datetime

spes = ['osteopathe', 'podologue', 'medecin', 'dentiste', 'pneumologue', 'cardiologue', 'gynecologue', 'ophtalmologue', 'orl', 'dermatologue']

departements = ['rhone-69','isere-38','loire-42','drome-26','haute-loire-43','ardeche-07']


for departement in departements:
    # Créons notre fichier de résultat csv

    resultFileName = 'scrap-pj' + '_' + str(datetime.datetime.now())[:-7] + '_' + departement +'.csv'
    result = open(resultFileName, 'w')
    resultWriter = csv.writer(result, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Contenu de la première ligne du tableau de résultats
    resultWriter.writerow(['Spécialité','Nom','Téléphone','Adresse'])

    compteur = 0

    for spe in spes:
        url = 'https://www.pagesjaunes.fr/annuaire/departement/' + departement +'/' + spe
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        prats = soup.select("div.zone-produit")

        for prat in prats:
            nom = prat.parent.a.get_text() 

            try:
                tel = prat.parent.find("strong", class_="num").get_text()
            except AttributeError:
                tel = "Non trouvé"
            adresse = prat.parent.find("a", class_="adresse").get_text()

            myRow = [spe, nom, tel, adresse]

            resultWriter.writerow(myRow)
            compteur += 1

    print('Travail terminé sur', departement, ', {0} prats ont été scrapés.'.format(compteur))
