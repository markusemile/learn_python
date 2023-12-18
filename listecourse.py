import json
from os import system,path
from colorama import Fore,Style

TITRE="Liste des courses"
MENU="""
1 - Ajouter un Article
2 - Enlever un Article
3 - Vider la liste
4 - Afficher la liste
5 - Sauver la liste

0 - Quitter

ps: N'oubliez pas de sauver avant de sortir.
"""
MENU_OPTIONS=["1","2","3","4","5","0"]
choix=None
liste=[]
chemin = "liste_course.json"

#initialisation de la liste ou création si elle existe pas
if path.exists(chemin):
    with open(chemin,"r") as f:
        liste=json.load(f)
else:
    with open(chemin,"w") as f:
        json.dump(liste,f,indent=4,ensure_ascii=False)



# function d'affichage du menu
def menu():
    system('cls')
    print(TITRE)
    print("*"*len(TITRE))
    print(MENU)

def title(titre):
    print(titre)
    print("*"*len(titre))



while choix!=0:
    menu()
    choix = input('Veuillez entrez votre choix [0-5] : ')
    if not choix.isdigit():
        print('Le choix doit être un numero ! ')
    elif choix not in MENU_OPTIONS:
        print(Fore.RED,'Veuillez choisir une option entre 0 et 5')
        print(Style.RESET_ALL)
        input("[ENTER]")
    else:
        choix = int(choix)
    
    if choix==1:
        article=None
        while article is None or len(article.strip())<1:
            system('cls')
            title("Ajout d'un article")
            article = input("Entrez l'article à ajouter : ")
            if len(article.strip())==0:
                print(Fore.RED,"Veuillez entrer un article !")
                print(Style.RESET_ALL)
                input("[enter]")
            else:
                liste.append(article)
        input("[enter]")

    elif choix==2:
        article=None
        while article is None:
            system('cls')
            title("Retirer un article")
            for i,item in enumerate(liste):
                print(f'{i} - {item}')        
            article = input('Veuillez choisir l\'article a retirer : ')
            if not article.isdigit():
                print(Fore.RED,'Les lettre et symbole ne sont pas accepté !')
                print(Style.RESET_ALL)
                input("[enter1]")
                article=None
            else:
                article_int = int(article)
                if  article_int >= len(liste) or article_int < 0:
                    print(Fore.RED,f'Veuillez choisir un article entre (0-{len(liste)-1})')
                    print(Style.RESET_ALL)
                    input("[enter2]")
                    article=None
                else:
                    liste.pop(article_int)
                    print(Fore.GREEN,'Article effacer avec success')
                    print(Style.RESET_ALL)
        input("[enter]")
    
    elif choix==3:
        liste.clear()
        print(Fore.RED,"Liste vider avec succès !!")
        print(Style.RESET_ALL)
    elif choix==4:
        system('cls')
        title("Afficghage de la liste")
        for item in liste:
            print(item)

        input("\n[enter]")

    elif choix==5:
        system('cls')
        title("Sauvegarde de la liste")
        with open(chemin,"w") as f:
            json.dump(liste,f,ensure_ascii=False,indent=4)
            print(Fore.GREEN,('Sauvegarde rélalisé avec succès'))
            print(Style.RESET_ALL)
        input("[ENTER]")

    

