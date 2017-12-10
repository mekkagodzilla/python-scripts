#!/usr/bin/python3
# -*- coding: utf-8 -*-

# second script pour manipuler du contenu html avec beautifulsoup.
# objectif : sortir une liste de prats réservables sur ubiclic

import requests, bs4, csv, datetime, re
from selenium import webdriver

baseUrl = 'https://www.ubiclic.com/'

spes = [
'medecine-generale',
'ophtalmologie',
]

villes = [
'grenoble', 
'lyon', 
#'saint-etienne', 'clermont-ferrand'
]


# Créons notre fichier de résultat csv

resultFileName = 'scrap-ubiclic' + '_' + str(datetime.datetime.now())[:-7] + '.csv'
result = open(resultFileName, 'w')
resultWriter = csv.writer(result, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
resultWriter.writerow(['Spécialité','Nom','Adresse','Code Postal', 'Ville', 'Profil']) # Contenu de la première ligne du tableau de résultats
compteur = 0

print('C’est parti pour le scrap Ubiclic' + str(villes) + str(spes))

for ville in villes:
    
    print(ville)

    for spe in spes:
        print('....' + spe) # petit print pour voir où en est le script quand il tourne
        url = baseUrl + spe + '/' + ville 
        browser = webdriver.PhantomJS() # le site charge le contenu du tableau de résultat en JS, on doit le feinter et lui faire croire qu'on est un vrai navigateur
        browser.get(url)
        html = browser.page_source
        soup = bs4.BeautifulSoup(html, 'lxml')
        prats = soup.select('div.pagepro') 


        for prat in prats:
            nom = prat.a.get_text()
            spans = prat.find_all('span')
            try:
                bigAdresse = spans[1].get('infobulle')
            except IndexError:
                bigAdresse = ''
            try:
                adresse, resVille = re.split('\d{5}', bigAdresse)
            except ValueError:
                adresse = bigAdresse
                resVille = bigAdresse.split(' ')[-1]
            try:
                codePostal = re.search('\d{5}', bigAdresse).group(0)
            except AttributeError:
                codePostal = 'Non disponible'
            profil = baseUrl  + prat.a.get('href')
        
            myRow = [spe, nom, adresse, codePostal, resVille, profil]
            resultWriter.writerow(myRow)
            compteur += 1

print('Travail terminé, {0} prats ont été scrapés.'.format(compteur))
