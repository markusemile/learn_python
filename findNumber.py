import random
import sys

mysternumber = random.randint(1,100)
essai = 0
max = 10
NOTGOOD=[]

def board():
    print('*'*50)
    print("* TE  * LIST OF NUMBER ")
    print('*'*50)
    print(f"* {essai}/{max} * {','.join(NOTGOOD)}")
    print('*'*50)
    print("\n")

while True:
    try:
        while essai<max:
            num  = int(input('Devinez le nombre... ? '))
            essai+=1
            NOTGOOD.append(str(num))
            if num == mysternumber:
                print(f"Bravo !!! vous avez trouber le nombre {mysternumber} en {essai} essai(s)")
                break
            else:
                board()
                if(num<mysternumber):
                    print("PLUS GRAND !!! Essaie encore!!")
                else:
                    print("PLUS PETIT !!! Essaie encore!!")
                continue
        print("Maximum d'essaie, vous avez perdu !!!")
        break
    except:
        print("Entrez une valeur numérique !")