

import CONFIGS
import turtle 



def file_handling(file):
    file_map = open(file, "r", encoding="utf-8")
    file_map = file_map.readlines()
    ret_map = []
    for line in file_map:
        line = line.replace(" ", "").replace("\n", "")
        elem_map = []
        for elem in line:
            elem_map.append(elem)
        ret_map.append(elem_map)
    return ret_map
        

def build_map():
    turtle.up()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0], CONFIGS.ZONE_PLAN_MAXI[1])
    size_box_lenght, size_box_width, angle = \
    (abs(CONFIGS.ZONE_PLAN_MINI[0]) + abs(CONFIGS.ZONE_PLAN_MAXI[0])) // len(CONFIGS.map[0]),(abs(CONFIGS.ZONE_PLAN_MINI[1]) + abs(CONFIGS.ZONE_PLAN_MAXI[1])) // len(CONFIGS.map[0]), 90
    CONFIGS.dimention_box = [size_box_lenght , size_box_width, angle]
    turtle.down()
    
    for line in range(len(CONFIGS.map)):
        for elem in range(len(CONFIGS.map[0])):
            box(line, elem, CONFIGS.dimention_box)
    turtle.up()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+(CONFIGS.POSITION_DEPART[1]*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                CONFIGS.ZONE_PLAN_MAXI[1]-(CONFIGS.POSITION_DEPART[0]*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
    
    turtle.dot(10, CONFIGS.COULEUR_PERSONNAGE)
    #indice()
    
    
    
def box(line, elem, dimention_box):
    digit = CONFIGS.map[line][elem]
    dict_color_box = {"0" : CONFIGS.COULEURS[0], "1" : CONFIGS.COULEURS[1], "2" : CONFIGS.COULEURS[2],
                  "3" : CONFIGS.COULEURS[3], "4" : CONFIGS.COULEURS[4]}
    
    color = dict_color_box[digit]
  
    turtle.up()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0] + (elem*dimention_box[0]), CONFIGS.ZONE_PLAN_MAXI[1] - (line*dimention_box[1]))
    turtle.speed(10)
    #turtle.down()
    
    for cote in range(2):
        turtle.tracer(0)
        turtle.begin_fill()
        turtle.color(color)
        turtle.fd(dimention_box[0])
        turtle.right(dimention_box[2])
        turtle.fd(dimention_box[1])
        turtle.right(dimention_box[2])
        turtle.end_fill()
    
def hide_dot():
    if CONFIGS.POSITION_DEPART == [-1, 1]:
        digit = 0
        color = CONFIGS.COULEURS[int(digit)]
    else:
        digit = CONFIGS.map[CONFIGS.POSITION_DEPART[0]][CONFIGS.POSITION_DEPART[1]]
        if CONFIGS.COULEURS[int(digit)] == CONFIGS.COULEURS[3]:
            turtle.dot(10, "red")
            
        if CONFIGS.COULEURS[int(digit)] == CONFIGS.COULEURS[4]:
            CONFIGS.map[CONFIGS.POSITION_DEPART[0]][CONFIGS.POSITION_DEPART[1]] = "0"
            box(CONFIGS.POSITION_DEPART[0], CONFIGS.POSITION_DEPART[1], CONFIGS.dimention_box)
    
        else:
            color = CONFIGS.COULEURS[int(digit)]
            turtle.dot(10, color)
    
    


def move():
    turtle.listen()    # Déclenche l’écoute du clavier
    turtle.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left une fonction appelée deplacer_gauche
    turtle.onkeypress(deplacer_droite, "Right")
    turtle.onkeypress(deplacer_haut, "Up")
    turtle.onkeypress(deplacer_bas, "Down")
    
    turtle.mainloop()    # Place le programme en position d’attente d’une action du joueur

def check_move():
    ret = 0 <= CONFIGS.POSITION_DEPART[0] < len(CONFIGS.map) and \
    0 <= CONFIGS.POSITION_DEPART[1] < len(CONFIGS.map[0]) and \
    CONFIGS.map[CONFIGS.POSITION_DEPART[0]][CONFIGS.POSITION_DEPART[1]] != "1"
    return ret
        

def deplacer_gauche():
    turtle.onkeypress(None, "Left")   # Désactive la touche Left
    # traitement associé à la flèche gauche appuyée par le joueur
    
    hide_dot()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+((CONFIGS.POSITION_DEPART[1]-1)*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                CONFIGS.ZONE_PLAN_MAXI[1]-((CONFIGS.POSITION_DEPART[0])*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
    CONFIGS.POSITION_DEPART = list(CONFIGS.POSITION_DEPART)
    CONFIGS.POSITION_DEPART[1] -= 1
    if check_move():
        turtle.dot(10, CONFIGS.COULEUR_PERSONNAGE)
    else:
        deplacer_droite()
    turtle.onkeypress(deplacer_gauche, "Left")   # Réassocie la touche Left à la fonction deplacer_gauche
    question(deplacer_droite)
    indice()
    tresor()



def deplacer_droite():
    #vérifier que le move est posible ...
    turtle.onkeypress(None, "Right")   # Désactive la touche Left
    # traitement associé à la flèche gauche appuyée par le joueur
    #cacher le dot
    
    hide_dot()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+((CONFIGS.POSITION_DEPART[1]+1)*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                CONFIGS.ZONE_PLAN_MAXI[1]-((CONFIGS.POSITION_DEPART[0])*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
    CONFIGS.POSITION_DEPART = list(CONFIGS.POSITION_DEPART)
    CONFIGS.POSITION_DEPART[1] += 1
    if check_move():
        turtle.dot(10, CONFIGS.COULEUR_PERSONNAGE)
    else:
        deplacer_gauche()
    turtle.onkeypress(deplacer_droite, "Right")   # Réassocie la touche Left à la fonction deplacer_gauche
    question(deplacer_gauche)
    indice()
    tresor()

def deplacer_haut():
    #vérifier que le move est posible ...
    turtle.onkeypress(None, "Up")   # Désactive la touche Left
    # traitement associé à la flèche gauche appuyée par le joueur
    
    hide_dot()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+((CONFIGS.POSITION_DEPART[1])*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                CONFIGS.ZONE_PLAN_MAXI[1]-((CONFIGS.POSITION_DEPART[0]-1)*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
    CONFIGS.POSITION_DEPART = list(CONFIGS.POSITION_DEPART)
    CONFIGS.POSITION_DEPART[0] -= 1
    if check_move():
        turtle.dot(10, CONFIGS.COULEUR_PERSONNAGE)
    else:
        deplacer_bas()
    turtle.onkeypress(deplacer_haut, "Up")   # Réassocie la touche Left à la fonction deplacer_gauche
    question(deplacer_bas)
    indice()
    tresor()


def deplacer_bas():
    #vérifier que le move est posible ...
    turtle.onkeypress(None, "Down")   # Désactive la touche Left
    # traitement associé à la flèche gauche appuyée par le joueur
    
    hide_dot()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+((CONFIGS.POSITION_DEPART[1])*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                CONFIGS.ZONE_PLAN_MAXI[1]-((CONFIGS.POSITION_DEPART[0]+1)*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
    CONFIGS.POSITION_DEPART = list(CONFIGS.POSITION_DEPART)
    CONFIGS.POSITION_DEPART[0] += 1
    if check_move():
        turtle.dot(10, CONFIGS.COULEUR_PERSONNAGE)
    else:
        deplacer_haut()
    turtle.onkeypress(deplacer_bas, "Down") # Réassocie la touche Left à la fonction deplacer_gauche
    question(deplacer_haut)
    indice()
    tresor()


def indice():
    for elem in CONFIGS.objet:
        if CONFIGS.POSITION_DEPART == [int(elem[0]), int(elem[1])]:
            message = CONFIGS.objet[elem[0], elem[1]]
            turtle.up()
            CONFIGS.POINT_AFFICHAGE_INVENTAIRE = list(CONFIGS.POINT_AFFICHAGE_INVENTAIRE)
            CONFIGS.POINT_AFFICHAGE_INVENTAIRE[1] -= 45
            pos = (CONFIGS.POINT_AFFICHAGE_INVENTAIRE[0], CONFIGS.POINT_AFFICHAGE_INVENTAIRE[1])
            turtle.goto(pos[0], pos[1])
            turtle.down()
            turtle.color("green")
            turtle.write(message, font=('Arial', 15, 'normal'))
            del CONFIGS.objet[elem[0], elem[1]]
            turtle.up()
            turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+(CONFIGS.POSITION_DEPART[1]*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                CONFIGS.ZONE_PLAN_MAXI[1]-(CONFIGS.POSITION_DEPART[0]*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
            break
            

def question(move):
    for elem in CONFIGS.portes:
        if CONFIGS.POSITION_DEPART == [int(elem[0]), int(elem[1])]:
            print(CONFIGS.portes[elem[0], elem[1]][1])
            turtle.up()
            turtle.goto(CONFIGS.POINT_AFFICHAGE_ANNONCES[0] - 200, CONFIGS.POINT_AFFICHAGE_ANNONCES[1])
            turtle.color("black")
            turtle.write("C'est porte est pour le moment fermé, répondé correctement à la question suivante pour l'ouvrir.", font=('Arial', 15, 'normal'))
            turtle.goto(CONFIGS.POINT_AFFICHAGE_ANNONCES[0] - 100, CONFIGS.POINT_AFFICHAGE_ANNONCES[1] - 20)
            turtle.write(CONFIGS.portes[elem[0], elem[1]][0], font=('Arial', 15, 'normal'))
            turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+(CONFIGS.POSITION_DEPART[1]*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                        CONFIGS.ZONE_PLAN_MAXI[1]-(CONFIGS.POSITION_DEPART[0]*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
            reponse = turtle.textinput("Question", CONFIGS.portes[elem[0], elem[1]][0])
            if reponse != None or reponse != "":
                reponse_correct = CONFIGS.portes[elem[0], elem[1]][1].replace("\'", "")
                if reponse == reponse_correct:
                    CONFIGS.map[CONFIGS.POSITION_DEPART[0]][CONFIGS.POSITION_DEPART[1]] = "0"
                    box(CONFIGS.POSITION_DEPART[0], CONFIGS.POSITION_DEPART[1], CONFIGS.dimention_box)
                    del CONFIGS.portes[elem[0], elem[1]]
                    turtle.up()
                    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+(CONFIGS.POSITION_DEPART[1]*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                        CONFIGS.ZONE_PLAN_MAXI[1]-(CONFIGS.POSITION_DEPART[0]*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)
                    turtle.dot(10, "red")
                    clear_annonceur()
                    break
            if reponse == None or reponse == "" or reponse != reponse_correct:
                move()
                clear_annonceur()
    

    turtle.listen()



def clear_annonceur():
    turtle.up()
    turtle.goto(CONFIGS.POINT_AFFICHAGE_ANNONCES[0] - 250, CONFIGS.POINT_AFFICHAGE_ANNONCES[1] + 20)
    turtle.color("white")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(1500)
        turtle.right(90)
        turtle.fd(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0]+(CONFIGS.POSITION_DEPART[1]*CONFIGS.dimention_box[0]) + CONFIGS.dimention_box[0] // 2,
                        CONFIGS.ZONE_PLAN_MAXI[1]-(CONFIGS.POSITION_DEPART[0]*CONFIGS.dimention_box[1]) - CONFIGS.dimention_box[1] // 2)

def tresor():
    digit = CONFIGS.map[CONFIGS.POSITION_DEPART[0]][CONFIGS.POSITION_DEPART[1]]
    if digit == "2":
        print("b")
        turtle.up()
        turtle.goto(CONFIGS.POINT_AFFICHAGE_ANNONCES[0], CONFIGS.POINT_AFFICHAGE_ANNONCES[1])
        turtle.color("black")
        turtle.down()
        message = "Bravo, tu as gagnée"
        turtle.write(message, font=('Arial', 20, 'normal'))








def creer_dictionnaires(fichier):
    file= open(fichier, "r", encoding="utf-8")
    file = file.readlines()
    ret = {}
    
    for objet in file:
        for elem in objet:
            objet = objet.replace("\n", "").replace("(", "").replace(")", "").replace("\"", "")
            clef, clef1, clef2, message = 0, "", "", ""
            for char in objet:
                if clef == 0:
                    if char != " ":
                        if char == ",":
                            clef += 1
                        else:
                            clef1 += char
                elif clef == 1:
                    if char != " ":
                        if char == ",":
                            clef += 1
                        else:
                            clef2 += char
                else:
                    message += char
            if fichier == CONFIGS.fichier_questions:
                cpt, liste = 0, []
                for i in range(len(message)-1, 0, -1):
                    if message[i] == ",":
                        cpt = len(message) - cpt
                        liste.append(message[0:cpt])
                        liste.append(message[cpt:])
                        liste[1] = liste[1].strip()
                    cpt += 1
                ret[clef1, clef2] = liste
            else:
                ret[clef1, clef2] = message 
    return ret


    
  
if __name__ == "__main__":
    turtle.listen()   
    file = CONFIGS.fichier_plan
    CONFIGS.map = file_handling(file)
    CONFIGS.objet = creer_dictionnaires(CONFIGS.fichier_objets)
    CONFIGS.portes = creer_dictionnaires(CONFIGS.fichier_questions)
    build_map()
    move()
    
    


