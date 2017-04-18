#! python3
# premier script pour manipuler du contenu html avec beautifulsoup.
# objectif : sortir une liste de prats réservables sur pjd

import requests, bs4, csv, datetime

spes = ['osteopathe', 'podologue', 'medecin', 'dentiste']

# Créons notre fichier de résultat csv

resultFileName = 'scrap-pj' + '_' + str(datetime.datetime.now())[:-7] + '.csv'
result = open(resultFileName, 'w')
resultWriter = csv.writer(result, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Contenu de la première ligne du tableau de résultats
resultWriter.writerow(['Spécialité','Nom','Téléphone','Adresse'])

compteur = 0

for spe in spes:
    url = 'https://www.pagesjaunes.fr/recherche/departement/rhone-69/' + spe
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

print('Travail terminé, {0} prats ont été scrapés.'.format(compteur))
