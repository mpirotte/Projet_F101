"""
Auteur : Martin Pirotte
Matricule : 000481569
Date : 26 Novembre 2018
But : Labyrinthe
Entrée : numéro du labyrinthe, droite ou gauche (dans le terminal)
Sorties : le labyrinthe : console et turtle
"""


import sys
import time
import turtle

MSG_BOUCLE = "Boucle détectée, cases visitées:"
MSG_SORTIE = "Sortie trouvée, cases visitées:"


##### FONCTION JEU PRINCIPAL ######

def lab_to_dic(f):
    """Converti le fichier texte, f, en dictionnaire ayant pour clée les coordonnées des caractères (" " ou #).
    Retourne également les dimensions du labyrinthe (le nombre de colones et de lignes) """

    dic = {}
    lig = 0
    for i in f:
        i = i.strip()
        col = 0
        for j in i:
            dic[(col, lig)] = j
            col += 1
        lig += 1
    return dic, lig, col


def print_ligne(dic, ligne, col):
    """permet d'imprimer une ligne du dictionnaire"""

    for i in range(col):
        print(dic[i, ligne], end="")


def print_lab(dic, col, lig):
    """imprime le dictionnaire en labyrinthe"""

    ligne = 0
    while ligne < lig:
        print_ligne(dic, ligne, col)
        print()
        ligne += 1


def recup_pos(dic):
    """récupère la position du pion dans le labyrinthe"""

    for i, j in dic.items():
        if j == 'v' or j == '<' or j == '>' or j == "^":
            colone, ligne = i
    return colone, ligne


def orient_pion_d(dic):
    """ fonction qui, si la personne a choisi de mettre sa main à droite, permet le
    déplacement du pion dans le labyrinthe en laissant sa "main" sur le mur de droite
    + oriente correctement le pion en turtle """

    c, l = recup_pos(dic)
    if dic[c, l] == "v":
        if dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
            turtle.right(90)
        elif dic[c, l + 1] == " ":
            dic[c, l + 1] = "v"
        elif dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
            turtle.left(90)
        elif dic[c, l + 1] == " ":
            dic[c, l] = "^"
            turtle.right(180)

    elif dic[c, l] == "^":
        if dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
            turtle.right(90)
        elif dic[c, l - 1] == " ":
            dic[c, l - 1] = "^"
        elif dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
            turtle.left(90)
        elif dic[c, l - 1] == " ":
            dic[c, l] = "v"
            turtle.right(180)

    elif dic[c, l] == ">":
        if dic[c, l + 1] == " ":
            dic[c, l + 1] = "v"
            turtle.right(90)
        elif dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
        elif dic[c, l - 1] == " ":
            dic[c, l - 1] = "^"
            turtle.left(90)
        elif dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
            turtle.right(180)

    elif dic[c, l] == "<":
        if dic[c, l - 1] == " ":
            dic[c, l - 1] = "^"
            turtle.right(90)
        elif dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
        elif dic[c, l + 1] == " ":
            dic[c, l + 1] = "v"
            turtle.left(90)
        elif dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
            turtle.right(180)

    dic[c, l] = " "
    return dic


def orient_pion_g(dic):
    """ fonction qui, si la personne a choisi de mettre sa main à gauche, permet le
       déplacement du pion dans le labyrinthe en laissant sa "main" sur le mur de gauche
       + oriente correctement le pion en turtle """
    c, l = recup_pos(dic)
    if dic[c, l] == "v":
        if dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
            turtle.left(90)
        elif dic[c, l + 1] == " ":
            dic[c, l + 1] = "v"
        elif dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
            turtle.right(90)
        elif dic[c, l + 1] == " ":
            dic[c, l] = "^"
            turtle.left(180)

    elif dic[c, l] == "^":
        if dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
            turtle.left(90)
        elif dic[c, l - 1] == " ":
            dic[c, l - 1] = "^"
        elif dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
            turtle.right(90)
        elif dic[c, l - 1] == " ":
            dic[c, l] = "v"
            turtle.left(180)

    elif dic[c, l] == ">":
        if dic[c, l - 1] == " ":
            dic[c, l - 1] = "^"
            turtle.left(90)
        elif dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
        elif dic[c, l + 1] == " ":
            dic[c, l + 1] = "v"
            turtle.right(90)
        elif dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
            turtle.left(180)

    elif dic[c, l] == "<":
        if dic[c, l + 1] == " ":
            dic[c, l + 1] = "v"
            turtle.left(90)
        elif dic[c - 1, l] == " ":
            dic[c - 1, l] = "<"
        elif dic[c, l - 1] == " ":
            dic[c, l - 1] = "^"
            turtle.right(90)
        elif dic[c + 1, l] == " ":
            dic[c + 1, l] = ">"
            turtle.left(180)

    dic[c, l] = " "
    return dic


def bloque(dic):
    """ fonction qui verifie que le pion ne soit pas dans une impasse"""

    c, l = recup_pos(dic)
    if dic[c, l] == "v" and dic[c - 1, l] == "#" and dic[c + 1, l] == "#" and dic[c, l + 1] == "#":
        res = True
    elif dic[c, l] == "^" and dic[c - 1, l] == "#" and dic[c + 1, l] == "#" and dic[c, l - 1] == "#":
        res = True
    elif dic[c, l] == "<" and dic[c, l + 1] == "#" and dic[c, l - 1] == "#" and dic[c - 1, l] == "#":
        res = True
    elif dic[c, l] == ">" and dic[c, l + 1] == "#" and dic[c, l - 1] == "#" and dic[c + 1, l] == "#":
        res = True
    else:
        res = False
    return res


def bloque_move(dic):
    """ mouvement a effectuer en fonction de l'orientation du pion,
     si celui si se trouve dans une impasse"""

    c, l = recup_pos(dic)
    if dic[c, l] == "v":
        dic[c, l - 1] = "^"
        turtle.right(180)
    elif dic[c, l] == "^":
        dic[c, l + 1] = "v"
        turtle.right(180)
    elif dic[c, l] == ">":
        dic[c - 1, l] = "<"
        turtle.right(180)
    elif dic[c, l] == "<":
        dic[c + 1, l] = ">"
        turtle.right(180)
    dic[c, l] = " "
    return dic


def chemin(dic, l):
    """ marque les cases parcouruent en console"""

    for i in l:
        dic[i] = "-"
    return dic

##### FONCTION TURTLE ####

def carre(l, x, y):
    """ dessine un carré vide de dimenssion l, de coordonnees x et y"""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.speed(0)

    for i in range(4):
        turtle.forward(l)
        turtle.right(90)


def carre_fin(l, x, y):
    """ dessine le chemin effectué en turtle"""
    turtle.color("red")
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.speed(0)

    for i in range(4):
        turtle.forward(l)
        turtle.right(90)

    turtle.end_fill()


def interface(dic, lig, col):
    """ initialise le labyrinthe en turtle """

    for j in range(lig):
        for k in range(col):
            if dic[k, j] == "#":
                turtle.begin_fill()
                carre(30, k * 30, j * -30)
                turtle.end_fill()
            else:
                carre(30, k * 30, j * -30)
    #place le pion à la position initiale
    turtle.up()
    turtle.goto(45, -15)
    turtle.down
    turtle.right(90)


########################################################

##### CODE PRINCIPAL ######

#definition des variables

f  = open(sys.argv[1])  #ouverture du fichier lab.txt
dic, lig, col = lab_to_dic(f) #creation du dico + nombre de colones et lignes
dic[1, 0] = "v" #place le pion à la position de départ
print_lab(dic, col, lig) #imprime le labyrinthe en console
l = [(1, 0)] #ajoute la position initiale à la liste des position
boucle = False
main_lab = sys.argv[2] #defini si on va suivre le mur de droite ou de gauche

interface(dic, lig, col) #imprime le labirynthe en turtle


#RESOLUTION du labyrinthe

while dic[col - 2, lig - 1] == " " and not boucle:
    #fait le deplacement en console
    #si on a choisi la droite
    if main_lab == 'd':
        if bloque(dic):
            bloque_move(dic)
        else:
            orient_pion_d(dic)

    #si on a choisi la gauche
    elif main_lab == 'g':
        if bloque(dic):
            bloque_move(dic)
        else:
            orient_pion_g(dic)

    #fait le deplacement en turtle
    x, y = recup_pos(dic)
    turtle.goto((x * 30) + (1 / 2 * 30), ((-y - 1) * 30) + (1 / 2 * 30))

    #imprime le "mouvement" effectué en console
    print()
    print_lab(dic, col, lig)
    time.sleep(0.3)
    a = recup_pos(dic)

    #si on est revenu a la position de départ
    if dic[1, 0] != " ":
        boucle = True
        l.append((1,0))
        dic[1,0] = " "
        dic[1,1] = "v"
        l.append((1, 1))

        print()
        print_lab(dic,col,lig)

    #sinon on ajoute les coordonnées de la case dans la liste des positions parcouruent
    else:
        l.append(a)

#si la sortie est trouvée ou si une boucle est detectée

print()
if boucle == True:
    print(MSG_BOUCLE)
    for i in range(len(l)):
        carre_fin(30, (l[i][0]) * 30, (l[i][1]+1) * -30) #trace le chemin en turtle
else:
    print(MSG_SORTIE)
    for i in range(len(l)):
        carre_fin(30, (l[i][0] + 1) * 30, l[i][1] * -30) #trace le chemin en turtle

print(l) #imprime la liste des positions

chemin(dic, l)
print_lab(dic, col, lig) #montre le parcours effectué
turtle.done()
f.close ()