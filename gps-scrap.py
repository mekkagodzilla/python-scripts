#!/usr/bin/python3
# -*- coding: utf-8 -*-

# second script pour manipuler du contenu html avec beautifulsoup.
# objectif : sortir une liste de prats réservables sur gps

import requests, bs4, csv, datetime, re
from selenium import webdriver

spes = ['pediatre','gynecologue', 'medecin-generaliste', 'ophtalmologue', 'chirurgien-dentiste', 'orl-oto-rhino-laryngologie', 'dermatologue-venerologue', 'angiologue', 'medecin-du-sport', 'endocrinologue-diabetologue', 'allergologue', 'sage-femme', 'cardiologue', ]

villes = ['clermont-ferrand', 'saint-martin-le-vinoux', 'lyon', 'saint-etienne']


# Créons notre fichier de résultat csv

resultFileName = 'scrap-gps' + '_' + str(datetime.datetime.now())[:-7] + '.csv'
result = open(resultFileName, 'w')
resultWriter = csv.writer(result, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
resultWriter.writerow(['Spécialité','Nom','Adresse', 'Profil']) # Contenu de la première ligne du tableau de résultats
compteur = 0

for ville in villes:
    
    print(ville)

    for spe in spes:
        url = 'http://www.gpssante.fr/' + spe + '/' + ville 
        browser = webdriver.PhantomJS() # le site charge le contenu du tableau de résultat en JS, on doit le feinter et lui faire croire qu'on est un vrai navigateur
        browser.get(url)
        html = browser.page_source
        soup = bs4.BeautifulSoup(html, 'lxml')
        prats = soup.find_all(id=re.compile('blockficheinfo_.')) #petite expression régulière pour attraper toutes les lignes du tableau de résultat
        print('....' + spe) # petit print pour voir où en est le script quand il tourne


        for prat in prats:
            nom = prat.a.get_text()[5:] # on tronque le début de la cellule contenant le nom, car elle commence par un retour chariot et 4 espaces
            adresse = prat.find("span", class_="margTop10").get_text()
            profil = 'http://www.gpssante.fr' + prat.a.get('href')
        
            myRow = [spe, nom, adresse, profil]
            resultWriter.writerow(myRow)
            compteur += 1

print('Travail terminé, {0} prats ont été scrapés.'.format(compteur))

