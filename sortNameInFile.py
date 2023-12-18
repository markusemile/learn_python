from pathlib import Path 
import os
import json
"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""
target = "./prenom.txt"

# try:
f= Path(target)
with open(f,"r",encoding="utf-8") as file:
    arr=file.read().splitlines()

prenoms=[]
for i in arr:
    prenoms.extend(i.split())

finalPrenoms = [prenom.strip(',. ') for prenom in prenoms ]

print(finalPrenoms)

with open("./prenomSorted.txt","w",encoding="utf-8") as fw:
    fw.write("\n".join(sorted(finalPrenoms)))