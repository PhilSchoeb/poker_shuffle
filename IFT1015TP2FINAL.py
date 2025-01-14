# Code de Philippe Schoeb et Juan Carlos Merida Cortes
# Dernière modification le 24 avril 2022

# Ce programme définit plusieurs fonctions et procédures pour faire un jeu de 
# poker shuffle.

import functools

# La fonction tab prend comme paramètre une valeur qui peut être convertie en 
# texte. Elle retourne un texte qui représente un tableau en html.

def tab(valeur):
    return '<table align="right">' + str(valeur) + '</table>'

# La fonction tr prend comme paramètre une valeur qui peut être convertie en 
# texte. Elle retourne un texte qui représente une rangée de tableau en html.

def tr(valeur):
    return '<tr>' + str(valeur) + '</tr>'

# La fonction td prend comme paramètre deux textes. Elle retourne un texte qui 
# représente une case de tableau en html. L'identifiant de la case est le 
# premier paramètre et ce qui y est affiché est le deuxième.

def td(id, inside):
    return '<td ' + id + '>' + inside + ' </td>'

# La fonction faireTableau n'a pas de paramètre et elle retourne un texte qui 
# représente un tableau de 25 cases vides en html.

def faireTableau():
    text = ""
    temp1 = []
    temp2 = ""
    image = '<img src="http://codeboot.org/cards/empty.svg"; onclick="clic('
    for i in range(5):
        for j in range(5):
            temp1.append(td('id="case' + str(j+1+i*5) + '"', image 
                           + str(j+1+i*5) + ')">'))
        
        temp2 += tr(''.join(temp1[i*5:(i+1)*5]))
    return tab(temp2)   

# La fonction htmlPoints n'a pas de paramètre et elle retourne un texte 
# représentant l'affichage, en html, des points des 5 rangées et 5 colonnes du 
# jeu.

def htmlPoints():
    texte = ''
    for i in range(10):
        texte += '<font id="points' + str(i+1) + '"; size="4"></font>'
    return texte
   

# La fonction genereOrdre n'a pas de paramètre et elle retourne un tableau 
# contenant les entiers de 0 à 51 mélangés aléatoirement. Elle simule le 
# mélange d'un paquet de carte.

def genereOrdre():
    paquet = list(range(52))
    for i in range(51, 1, -1):
        j = math.floor(random() * (i + 1))
        temp = paquet[i]
        paquet[i] = paquet[j]
        paquet[j] = temp        
    return paquet

# La fonction associerNbreCarte a comme seul paramètre un entier plus petit 
# que 52 et elle retourne un texte qui représente la carte associée à l'entier 
# en paramètre.

def associerNbreCarte(n):
    if n < 0:
        return 'empty'
    
    numero = (n // 4) + 1
    if numero == 1:
        numero = 'A'
    elif numero == 11:
        numero = 'J'
    elif numero == 12:
        numero = 'Q'
    elif numero == 13:
        numero = 'K'
        
    famille = n % 4
    if famille == 0:
        famille = 'C'
    elif famille == 1:
        famille = 'D'
    elif famille == 2:
        famille = 'H'
    elif famille == 3:
        famille = 'S'
        
    carte = str(numero) + famille
    return carte

# Je me suis inspiré d'une vidéo pour inclure le fond vers lime dans le style 
# à l'aide du '.someStyle'. Voici le lien :
# https://www.youtube.com/watch?v=Ff8MraDWbGU&ab_channel=AdamKhoury
html = '''<style> #case0 { position: absolute; left : 180px; top : 50px; } 
                  #bouton { position: absolute; left : 20px; top : 75px; }
                  #points1 { position: absolute; left : 930px; top : 115px; }
                  #points2 { position: absolute; left : 930px; top : 250px; }
                  #points3 { position: absolute; left : 930px; top : 385px; }
                  #points4 { position: absolute; left : 930px; top : 520px; }
                  #points5 { position: absolute; left : 930px; top : 655px; }
                  #points6 { position: absolute; left : 445px; top : 750px; }
                  #points7 { position: absolute; left : 545px; top : 750px; }
                  #points8 { position: absolute; left : 645px; top : 750px; }
                  #points9 { position: absolute; left : 745px; top : 750px; }
                  #points10 { position: absolute; left : 845px; top : 750px; }
                  #pointage { position: absolute; left : 930px; top : 750px; }
                  .someStyle{background-color: lime;} </style>
<button id="bouton"; onclick="init()">Nouvelle partie</button>
<div id="case0"><img src="http://codeboot.org/cards/back.svg"; height="138"; 
onclick="clic(0)"></div>
<style>
        #main table td { border: 0; padding: 1px 2px; }
        #main table td img { height: auto; }
        #main table { position: absolute; left : 400px; top : 50px; }
      </style>''' + faireTableau() + '''<font id="pointage"; 
      size="10">0</font>''' + htmlPoints()

# La procédure init n'a pas de paramètre et elle ne retourne rien. Elle 
# définit 5 variables globales importantes et insère le texte html dans le 
# main. Elle simule un début de partie.

def init():
    # tabJeu est un tableau de 25 entiers qui représente les cartes placées. 
    # Le nombre -1 représente l'absence de carte.
    global tabJeu 
    
    # carteJeuSelec est un tableau de 2 éléments. Le premier est un booléen 
    # qui indique si une carte sur le jeu est sélectionnée (cela exclue la 
    # pile de cartes). Le deuxième est un texte qui représente quelle carte 
    # est sélectionnée.
    global carteJeuSelec 
    global cartePileSelec # Booléen qui indique si la pile est sélectionnée.
    
    # nbCarte est un entier qui indique combien de cartes de la pile ont été 
    # tournées.
    global nbCartes 
    global ordre # Tableau qui représente l'ordre du paquet.
    
    tabJeu = list(map(lambda i: -1, range(25)))
    carteJeuSelec = [False, '']
    cartePileSelec = False
    nbCartes = 0
    ordre = genereOrdre()
    
    main = document.querySelector('#main')
    main.innerHTML = html
    
init()

# La procédure selection prend comme paramètre un texte qui représente un 
# identifiant html. Elle ne retourne rien mais elle applique une couleur de 
# fond vert lime à l'objet identifié.

def selection(id): 
    document.querySelector(id).setAttribute('class', 'someStyle')
    return
       
    
# La procédure deselection prend comme paramètre un texte qui représente un
# identifiant html. Elle ne retourne rien mais elle retire l'attribut class de 
# l'objet identifié. Dans ce programme elle sert seulement à enlever la 
# couleur de fond vert.
    
def deselection(id): # on pourra enlever le if else je pense
    document.querySelector(id).removeAttribute('class')
    return

# La procédure clicPile a comme paramètre un booléen qui est True si une carte 
# est déjà affichée sur la pile et False si c'est le dos d'une carte. Elle ne 
# retourne rien mais elle modifie l'affichage et l'état du jeu après un clic 
# sur la pile.

def clicPile(dejaCarte):
    global nbCartes
    global cartePileSelec
    global ordre
    
    if dejaCarte:
        if cartePileSelec:
            cartePileSelec = False
            deselection('#case0')
        else:
            cartePileSelec = True
            selection('#case0')
            
    else: # Cliquer sur le dos de la carte
        carte = int(ordre[nbCartes])
        nbCartes += 1
        txt1 = '<img src="http://codeboot.org/cards/'
        txt2 = '.svg"; height="138"; onclick="clic(0)">'
        html = txt1 + associerNbreCarte(carte) + txt2
        document.querySelector('#case0').innerHTML = html
        cartePileSelec = True
        selection('#case0')
        
    return

# La procédure clicCaseVidePileSelec a comme paramètre l'identifiant de la 
# case cliquée et elle ne retourne rien. Elle intervient quand il y a un clic 
# sur une case vide pendant qu'une carte de la pile est sélectionnée. Elle 
# modifie l'affichage et l'état du jeu en conséquence.

def clicCaseVidePileSelec(id):
    global cartePileSelec
    global nbCartes
    global ordre
    global tabJeu
    global htmlDos
    
    document.querySelector('#case0').innerHTML = htmlDos
    
    n = int(id[5:]) # id de la forme '#caseN' avec N un naturel
    carte = int(ordre[nbCartes - 1])
    txt1 = '<img src="http://codeboot.org/cards/'
    txt2 = '.svg"; onclick='
    fonctionClic = '"clic(' + str(n) + ')">'
    html = txt1 + associerNbreCarte(carte) + txt2 + fonctionClic
    document.querySelector(id).innerHTML = html
    
    cartePileSelec = False
    deselection('#case0')
    tabJeu[n-1] = carte
    
    return 

# La procédure clicJeuSelec a comme paramètres un texte qui est l'identifiant 
# de la case cliquée ainsi qu'un booléen qui est True si la case cliquée est 
# vide et False si elle contient déjà une carte. Elle ne retourne rien mais 
# elle modifie l'affichage et l'état du jeu. Elle est appelée quand une carte 
# en jeu est sélectionnée et qu'un clic à lieu sur une autre carte en jeu.
    
def clicJeuSelec(id, caseVide):
    global carteJeuSelec
    global tabjeu
    
    n = int(id[5:]) # id de la forme '#caseN' avec N un naturel
    temp1 = document.querySelector(carteJeuSelec[1]).innerHTML 
    temp2 = document.querySelector(id).innerHTML
    
    txt1 = '<img  src="http://codeboot.org/cards/empty.svg"; onclick="clic('
    # Dans ce programme, carteJeuSelec[1] est toujours de la forme '#caseN' où 
    # N est un naturel entre 0 et 25. Donc carteJeuSelec[1][5:] est le naturel 
    # qui représente la case sélectionnée.
    htmlVide = txt1 + carteJeuSelec[1][5:] + ')">'
    
    document.querySelector(id).innerHTML = temp1[0:44] + temp2[45:] 
    if caseVide:
        document.querySelector(carteJeuSelec[1]).innerHTML = htmlVide
    else:
        temp = temp2[0:44] + temp1[45:]
        document.querySelector(carteJeuSelec[1]).innerHTML = temp
  
    temp3 = tabJeu[int(carteJeuSelec[1][5:])-1]
    temp4 = tabJeu[n-1]
    
    tabJeu[n-1] = temp3
    tabJeu[int(carteJeuSelec[1][5:])-1] = -1 if caseVide else temp4
    
    deselection(carteJeuSelec[1])
    carteJeuSelec = [False, '']
    
    return

# La procédure clic prend en paramètre un nombre naturel de 0 à 25 qui 
# représente quelle case a été cliquée. Elle ne retourne rien, par contre elle 
# s'occupe de changer l'affichage du jeu et elle modifie aussi certaines 
# variables globales pour enregistrer l'état du jeu.

def clic(n):
    global cartePileSelec
    global carteJeuSelec
    global nbCartes
    global ordre
    global tabJeu
    global htmlDos
    
    htmlDos = '<img src="http://codeboot.org/cards/back.svg" ;="" height'
    htmlDos += '="138" onclick="CodeBoot.prototype.event_handle(event,1)">'
    id = '#case' + str(n)
    
    if n == 0: # Clic sur la pile de cartes
        if carteJeuSelec[0]: # Si une carte du jeu est sélectionnée.
            deselection(carteJeuSelec[1])
            carteJeuSelec = [False, '']
   
        dejaCarte = document.querySelector(id).innerHTML != htmlDos
        clicPile(dejaCarte) 
        
    else: # Clic sur une case du jeu
        caseVide = tabJeu[n-1] == -1
        
        if cartePileSelec: # Si une carte de la pile est sélectionnée
            
            if caseVide: # Si la case cliquée est vide
                clicCaseVidePileSelec(id)
                
            else: # Si la case cliquée contient déjà une carte
                selection(id)
                carteJeuSelec = [True, id]
                deselection('#case0')
                cartePileSelec = False
                
        else: # Si la carte de la pile n'est pas sélectionnée
            
            # Si aucune carte en jeu n'est sélectionnée aussi.
            if not(carteJeuSelec[0]):
                if not(caseVide): # Si la case cliquée contient une carte
                    selection(id)
                    carteJeuSelec = [True, id]
                    
            else: # Si une carte en jeu est sélectionnée (excluant la pile)
                
                # Si la carte cliquée est déjà sélectionnée.
                if carteJeuSelec[1] == '#case' + str(n):
                    deselection(id)
                    carteJeuSelec = [False, '']
                    
                else: # Si la carte cliquée n'est pas celle sélectionnée
                    clicJeuSelec(id, caseVide)
                
    jeu()
    return        
    
# La procédure jeu n'a pas de paramètre et ne retourne rien. Elle appelle 
# plusieurs fonctions pour calculer, afficher les points et elle annonce la 
# fin d'une partie.        

def jeu():
    global nbCartes
    global htmlDos
   
    tabMains = constructionMainPoker(tabJeu)
    tabMainsOrd = ordreCroissant(tabMains)
    mainsPoints = pointsParMain(tabMainsOrd)
    
    # Afficher le total de points
    total = functools.reduce(lambda x,y: x+y, mainsPoints)
    document.querySelector('#pointage').innerHTML = str(total)
    
    # Afficher les points des mains de poker
    for i in range(10):
        affichePoints(mainsPoints, i)
    
    fin1 = nbCartes == 25
    fin2 = document.querySelector('#case0').innerHTML == htmlDos
    if fin1 and fin2:
        sleep(0.25)
        message = 'Partie terminée! Bravo, tu as fait ' + str(total)
        message += ' points!'
        alert(message)
        init()
    return
        

# La fonction constructionMainPoker a comme paramètre un tableau de 25 
# éléments qui représente le contenu des 25 cases de jeu. Elle retourne un 
# tableau de 10 tableaux contenant 5 entiers chacun. Chacun des 10 tableaux 
# représente une main de poker. Les 5 premiers tableaux représentent les 5 
# rangées du jeu et les 5 autres représentent les 5 colonnes.

def constructionMainPoker(tabJeu):
    tabMains = list(map(lambda i: [], range(10)))
    
    for i in range(10):
        if i <= 4:
            tabMains[i] = tabJeu[i*5:(i+1)*5]
        else:
            tabMains[i] = tabJeu[i-5::5]
            
    return tabMains    
    
# La fonction fusion est directement prise des notes de cours au chapitre 13, 
# diapositive 67. Elle prend comme paramètres 2 tableaux de nombres en ordre 
# croissant et elle retourne un tableau contenant tous les éléments des deux 
# tableaux en ordre croissant.

def fusion(liste1, liste2): 
    resultat = []
    i = 0 # index du prochain élément de liste1
    j = 0 # index du prochain élément de liste2
    while i < len(liste1) and j < len(liste2):
        if liste1[i] < liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1
            
    while i < len(liste1): resultat.append(liste1[i]) ; i += 1
    while j < len(liste2): resultat.append(liste2[j]) ; j += 1
    return resultat        

# La fonction trier est directement prise des notes de cours au chapitre 13,
# diapositive 68. Elle prend en paramètre un tableau de nombres et elle 
# retourne le même tableau mais avec ses éléments en ordre croissant.

def trier(liste):
    if len(liste) <= 1:
        return liste.copy()
    else: # Par récursion
        milieu = len(liste) // 2
        tri1 = trier( liste[:milieu] )
        tri2 = trier( liste[milieu:] )
        return fusion(tri1, tri2)



# La fonction ordreCroissant a comme paramètre un tableau de 10 tableaux 
# contenant 5 entiers et elle retourne le même tableau sauf que les éléments 
# de chacun des 10 tableaux sont placés en ordre croissant.

def ordreCroissant(tabMains):
    nouvTab = list(map(lambda i: 0, range(10)))
    for i in range(len(tabMains)):
        nouvTab[i] = trier(tabMains[i]) 
    return nouvTab
    

# La fonction pointsParMain prend en paramètre un tableau de 10 tableaux 
# contenant chacun 5 entiers en ordre croissant. Elle retourne un tableau de 
# 10 entiers qui représente le nombre de points par mains.

def pointsParMain(tabMains): 
    tabPoints1 = verifMemeCouleur(tabMains) 
    tabPoints2 = verifQuinte(tabMains)
    tabPoints3 = verifPaire(tabMains)
    # On prend le maximum car quand une main est associée à plusieurs 
    # pointages, on ne considère que le plus grand.
    tabPoints = list(map(lambda i: max(tabPoints1[i], tabPoints2[i], 
                                       tabPoints3[i]), range(10)))
    return tabPoints
    

# La fonction verifPaire prend en paramètre un tableau de 10 tableaux 
# contenant 5 entiers et elle retourne un tableau de 10 entiers qui représente 
# le nombre de points accordé à chaque main qui est associé à une paire de 
# cartes de même valeur. Les mains de poker détectées par cette fonction 
# comprennent toutes au moins une paire. Elle détecte les paires, doubles 
# paires, brelans, full house et carrés.
                     
def verifPaire(tabMains): 
    tabPoints = list(map(lambda k: 0, range(10)))
                     
    for i in range(len(tabMains)):
        car1 = tabMains[i][0] // 4
        car2 = tabMains[i][1] // 4
        car3 = tabMains[i][2] // 4
        car4 = tabMains[i][3] // 4
        car5 = tabMains[i][4] // 4
                     
        if car1 == car2 != -1: # Au moins une paire
            tabPoints[i] = 2
                     
            if car3 == car1: # Au moins un brelan
                tabPoints[i] = 10
                     
                if car4 == car1: # Carré
                    tabPoints[i] = 50
                     
                else:
                    if car4 == car5 != -1: # Full house
                        tabPoints[i] = 25
                     
            else:
                if car3 == car4 != -1: # Au moins 2 paires
                    tabPoints[i] = 5
                     
                    if car5 == car3: # Full house
                        tabPoints[i] = 25
                     
                else:
                    if car4 == car5 != -1: # 2 paires
                        tabPoints[i] = 5
                     
        elif car2 == car3 != -1: # Au moins une paire
            tabPoints[i] = 2
                     
            if car4 == car2: # Au moins un brelan
                tabPoints[i] = 10
                     
                if car5 == car2:# Carré
                    tabPoints[i] = 50
                     
            elif car4 == car5 != -1: # Double paire
                tabPoints[i] = 5
                     
        elif car3 == car4 != -1: # Au moins une paire
            tabPoints[i] = 2
                     
            if car5 == car3: # Brelan
                tabPoints[i] = 10
                     
        elif car4 == car5 != -1: # Paire
            tabPoints[i] = 2
                     
    return tabPoints
         
# La fonction verifQuinte prend en paramètre un tableau de 10 tableaux
# contenant 5 entiers et elle retourne un tableau de 10 entiers qui représente 
# le nombre de points accordé à chaque main qui vient d'une quinte. Cette 
# fonction ne détecte pas les quintes flush et les quintes flush royales.           
                   
def verifQuinte(tabMains):
    tabPoints = list(map(lambda k: 0, range(10)))
                     
    for i in range(len(tabMains)):
        if tabMains[i][0] == -1:
            continue
                     
        car1 = tabMains[i][0] // 4
        car2 = tabMains[i][1] // 4
        car3 = tabMains[i][2] // 4
        car4 = tabMains[i][3] // 4
        car5 = tabMains[i][4] // 4
                     
        if car5 == car4 + 1 == car3 + 2 == car2 + 3 == car1 + 4:
            tabPoints[i] = 15
                     
        elif car1 == 0: # Commence par un as
            if car5 == car4 + 1 == car3 + 2 == car2 + 3 == 12:
                tabPoints[i] = 15
                     
    return tabPoints
   

                     
# La fonction verifMemeCouleur prend en paramètre un tableau de 10 tableaux 
# contenant 5 entiers et elle retourne un tableau de 10 entiers qui représente 
# le nombre de points accordé à chaque main qui est associé à une couleur. Par 
# couleur on entend 5 cartes de même symbole/famille. Les mains de poker 
# détectées par cette fonction comprennent toutes au moins une couleur. Elle 
# détecte les couleurs, quintes flush et quintes flush royales.                     
                     
def verifMemeCouleur(tabMains): 
    tabPoints = list(map(lambda k: 0, range(10)))
                     
    for i in range(len(tabMains)):
        if tabMains[i][0] == -1:
            continue
                     
        coul1 = tabMains[i][0] % 4
        coul2 = tabMains[i][1] % 4
        coul3 = tabMains[i][2] % 4
        coul4 = tabMains[i][3] % 4
        coul5 = tabMains[i][4] % 4
        car1 = tabMains[i][0] // 4
        car2 = tabMains[i][1] // 4
        car3 = tabMains[i][2] // 4
        car4 = tabMains[i][3] // 4
        car5 = tabMains[i][4] // 4
                     
        if coul1 == coul2 == coul3 == coul4 == coul5:
            tabPoints[i] = 20
                     
            if car1 == 0: # Commence par un as
                if car5 == car4 + 1 == car3 + 2 == car2 + 3 == 4:
                    tabPoints[i] = 75 # Quinte flush
                     
                else:
                    flushRoyale = [0, 9, 10, 11, 12]
                    tabCar = [car1, car2, car3, car4, car5] 
                     
                    if tabCar == flushRoyale:
                        tabPoints[i] = 100
            else:
                if car5 == car4 + 1 == car3 + 2 == car2 + 3 == car1 + 4:
                    tabPoints[i] = 75 # Quinte flush

    return tabPoints                   
    
# La procédure affichePoints prend comme paramètre un tableau contenant 10 
# entiers et un nombre naturel entre 0 et 9. Elle ne retourne rien, mais elle 
# modifie l'affichage du pointage de la main de poker associée à l'entier en 
# deuxième paramètre. 

def affichePoints(tabPoints, i):
    id = '#points' + str(i + 1)
   
    if tabPoints[i] != 0:
        document.querySelector(id).innerHTML = str(tabPoints[i])
        
    else:
        document.querySelector(id).innerHTML = ''
        
    return    
                   
# La procédure testPoker n'a pas de paramètre et ne retourne rien. Elle 
# s'occupe des tests unitaires.

def testPoker():
    
    # Test tab
    assert tab('allo') == '<table align="right">allo</table>'
    assert tab(10) == '<table align="right">10</table>'
    assert tab('') == '<table align="right"></table>'
    
    # Test tr
    assert tr('allo') == '<tr>allo</tr>'
    assert tr(10) == '<tr>10</tr>'
    assert tr('') == '<tr></tr>'
    
    # Test td
    assert td('id="case0"', 'ok') == '<td id="case0">ok </td>'
    assert td('10', 'UwU') == '<td 10>UwU </td>'
    assert td('', '') == '<td > </td>'
    
    # Test faireTableau
    txt = '<table align="right"><tr><td id="case1"><img '
    txt += 'src="http://codeboot.org/cards/empty.svg"; onclick="clic(1)"> '
    txt += '</td><td id="case2"><img src="http://codeboot.org/cards/'
    txt += 'empty.svg"; onclick="clic(2)"> </td><td id="case3"><img '
    txt += 'src="http://codeboot.org/cards/empty.svg"; onclick="clic(3)"> '
    txt += '</td><td id="case4"><img src="http://codeboot.org/cards/'
    txt += 'empty.svg"; onclick="clic(4)"> </td><td id="case5"><img '
    txt += 'src="http://codeboot.org/cards/empty.svg"; onclick="clic(5)"> '
    txt += '</td></tr><tr><td id="case6"><img src="http://codeboot.org/'
    txt += 'cards/empty.svg"; onclick="clic(6)"> </td><td id="case7"><img '
    txt += 'src="http://codeboot.org/cards/empty.svg"; onclick="clic(7)"> '
    txt += '</td><td id="case8"><img src="http://codeboot.org/cards/'
    txt += 'empty.svg"; onclick="clic(8)"> </td><td id="case9"><img '
    txt += 'src="http://codeboot.org/cards/empty.svg"; onclick="clic(9)"> '
    txt += '</td><td id="case10"><img src="http://codeboot.org/cards/'
    txt += 'empty.svg"; onclick="clic(10)"> </td></tr><tr>'
    txt += '<td id="case11"><img src="http://codeboot.org/cards/empty.svg"; '
    txt += 'onclick="clic(11)"> </td><td id="case12"><img src="http://'
    txt += 'codeboot.org/cards/empty.svg"; onclick="clic(12)"> </td>'
    txt += '<td id="case13"><img src="http://codeboot.org/cards/empty.svg"; '
    txt += 'onclick="clic(13)"> </td><td id="case14"><img src="http://'
    txt += 'codeboot.org/cards/empty.svg"; onclick="clic(14)"> </td>'
    txt += '<td id="case15"><img src="http://codeboot.org/cards/empty.svg"; '
    txt += 'onclick="clic(15)"> </td></tr><tr><td id="case16">'
    txt += '<img src="http://codeboot.org/cards/empty.svg"; '
    txt += 'onclick="clic(16)"> </td><td id="case17"><img src="http://'
    txt += 'codeboot.org/cards/empty.svg"; onclick="clic(17)"> </td>'
    txt += '<td id="case18"><img src="http://codeboot.org/cards/empty.svg"; '
    txt += 'onclick="clic(18)"> </td><td id="case19"><img src="http://'
    txt += 'codeboot.org/cards/empty.svg"; onclick="clic(19)"> </td>'
    txt += '<td id="case20"><img src="http://codeboot.org/cards/'
    txt += 'empty.svg"; onclick="clic(20)"> </td></tr><tr>'
    txt += '<td id="case21"><img src="http://codeboot.org/cards/empty.svg"; '
    txt += 'onclick="clic(21)"> </td><td id="case22"><img src="http://'
    txt += 'codeboot.org/cards/empty.svg"; onclick="clic(22)"> '
    txt += '</td><td id="case23"><img src="http://codeboot.org/'
    txt += 'cards/empty.svg"; onclick="clic(23)"> </td><td id="case24">'
    txt += '<img src="http://codeboot.org/cards/empty.svg"; '
    txt += 'onclick="clic(24)"> </td><td id="case25"><img src="http://'
    txt += 'codeboot.org/cards/empty.svg"; onclick="clic(25)"> </td></tr>'
    txt += '</table>'
    
    assert faireTableau() == txt
    
    # Test genereOrdre
    assert len(genereOrdre()) == 52
    bool = False
    paquet = genereOrdre()
    for i in range(52):
        if paquet[i] == 10:
            bool = not(bool)
    assert bool
    for i in range(52):
        if paquet[i] >= 52:
            bool = False
    assert bool
    
    # Test associerNbreCarte
    assert associerNbreCarte(-1) == 'empty'
    assert associerNbreCarte(6) == '2H'
    assert associerNbreCarte(51) == 'KS'
    assert associerNbreCarte(0) == 'AC'
    assert associerNbreCarte(-11) == 'empty'
    
    # Test htmlPoints
    txt2 = '<font id="points1"; size="4"></font><font id="points2"; size="4">'
    txt2 += '</font><font id="points3"; size="4"></font><font id="points4"; '
    txt2 += 'size="4"></font><font id="points5"; size="4"></font>'
    txt2 += '<font id="points6"; size="4"></font><font id="points7"; '
    txt2 += 'size="4"></font><font id="points8"; size="4"></font>'
    txt2 += '<font id="points9"; size="4"></font><font id="points10"; '
    txt2 += 'size="4"></font>'
    
    assert htmlPoints() == txt2
    
    # Test constructionMainPoker
    tabJeu1 = [1] * 25
    tabJeu2 = [1,2,3,4,5] * 5
    tabJeu3 = [456, 34, 32, 2, 0, 5, 5, 3, 4, 5, 6, 6, 54, 5, 6, 7, 77, 54, 5]
    tabJeu3 += [44, 2, 22, 12, 3, 12]
    tabJeu4 = [0] * 25
    assert constructionMainPoker(tabJeu1) == [[1,1,1,1,1]] * 10
    tab2 = [[1,2,3,4,5]] * 5 + [[1] * 5] + [[2] * 5] + [[3] * 5] + [[4] * 5] 
    tab2 += [[5] * 5]
    assert constructionMainPoker(tabJeu2) == tab2
    tab3 = [[456, 34, 32, 2, 0], [5, 5, 3, 4, 5], [6, 6, 54, 5, 6], 
            [7, 77, 54, 5, 44], [2, 22, 12, 3, 12], [456, 5, 6, 7, 2], 
            [34, 5, 6, 77, 22], [32, 3, 54, 54, 12], [2, 4, 5, 5, 3], 
            [0, 5, 6, 44, 12]]
    assert constructionMainPoker(tabJeu3) == tab3
    assert constructionMainPoker(tabJeu4) == [[0,0,0,0,0]] * 10
    
    # Test fusion
    assert fusion([], []) == []
    assert fusion([0,0], [0,0,0]) == [0] * 5
    assert fusion([1,2,3], [1,2,3]) == [1,1,2,2,3,3]
    assert fusion([1,23,100], [-3,22,109]) == [-3,1,22,23,100,109]
    assert fusion([1.23, 1.24], [5/4]) == [1.23, 1.24, 1.25]
    
    # Test trier
    assert trier([]) == []
    assert trier([-2, 0, 2, 5, 6.7]) == [-2, 0, 2, 5, 6.7]
    assert trier([1, 0, -1, 1/3]) == [-1, 0, 1/3, 1]
    assert trier([100]) == [100]
    
    # Test ordreCroissant
    assert ordreCroissant([[1,2,3,4,5]]*10) == [[1,2,3,4,5]] * 10
    # Réutilisons tab3 définit ci-haut
    tab3Croiss = [[0, 2, 32, 34, 456], [3, 4, 5, 5, 5], [5, 6, 6, 6, 54], 
                  [5, 7, 44, 54, 77], [2, 3, 12, 12, 22], [2, 5, 6, 7, 456], 
                  [5, 6, 22, 34, 77], [3, 12, 32, 54, 54], [2, 3, 4, 5, 5], 
                  [0, 5, 6, 12, 44]]
    assert ordreCroissant(tab3) == tab3Croiss
    assert ordreCroissant([[1,1,1,-1,1]] * 10) == [[-1,1,1,1,1]] * 10
                     
    # Test verifPaire
    assert verifPaire([[-1,-1,-1,-1,-1] * 10]) == [0,0,0,0,0,0,0,0,0,0]
    tabMain1 = [[1,2,3,14,15], [4,5,17,18,40], [0,2,3,23,50]]
    tabMain1 += [[16,17,18,19,33], [-1]*5, [12,20,24,30,40], [21,22,26,44,51]]
    tabMain1 += [[12,32,33,34, 49], [-1,11,12,13,17], [21,22,45,46,47]]
    assert verifPaire(tabMain1) == [25, 5, 10, 50, 0, 0, 2, 10, 2, 25]
    
    # Test verifQuinte
    assert verifQuinte([[-1,-1,-1,-1,-1]] * 10) == [0,0,0,0,0,0,0,0,0,0]
    tabMain2 = [[1,5,9,13,17], [1,4,11,12,18], [3,37,41,47,48]]
    tabMain2 += [[16,17,18,19,33], [-1]*5, [12,20,24,30,40], [24,28,37,38,40]]
    tabMain2 += [[3,39,43,47,51], [0,1,2,3,4], [-1,22,25,31,33]]
    assert verifQuinte(tabMain2) == [15, 15, 15, 0, 0, 0, 0, 15, 0, 0]
    
    # Test verifMemeCouleur
    assert verifMemeCouleur([[-1,-1,-1,-1,-1]] * 10) == [0,0,0,0,0,0,0,0,0,0]
    tabMain3 = [[1,5,9,13,17], [-1,1,5,9,25], [0,12,24,44,48]]
    tabMain3 += [[2,38,42,46,50], [-1]*5, [2,38,42,46,51], [34,38,42,46,50]]
    tabMain3 += [[7,19,23,39,51], [47,48,49,50,51], [32,34,36,38,40]]
    assert verifMemeCouleur(tabMain3) == [75, 0, 20, 100, 0, 0, 75, 20, 0, 0]
    
    # Test pointsParMain
    assert pointsParMain([[-1,-1,-1,-1,-1]] * 10) == [0,0,0,0,0,0,0,0,0,0]
    tabMain4 = [[1,5,9,13,17], [-1,1,3,9,25], [0,12,24,44,48]]
    tabMain4 += [[2,38,42,46,50], [3,7,12,40,51], [2,38,42,46,51]]
    tabMain4 += [[36,37,39,46,47], [8,9,10,11,51], [40,46,47,50,51]]
    tabMain4 += [[31,33,34,35,40]]
    assert pointsParMain(tabMain4) == [75, 2, 20, 100, 0, 15, 25, 50, 5, 10]
    
testPoker()    

