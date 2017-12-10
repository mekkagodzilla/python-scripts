import re

mystring = '180 cours Emile Zola immeuble Le Saphir Métro Gratte-Ciel 2ème étage , 69100 VILLEURBANNE'

mysplit = re.split("\d{5}", mystring)

print(mysplit)
mycode = re.search('\d{5}', mystring)
print(mycode.group(0))

resVille = mystring.split(' ')[-1]
print(resVille)
