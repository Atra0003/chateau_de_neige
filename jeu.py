
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
    
    
    
def box(line, elem, dimention_box):
    digit = CONFIGS.map[line][elem]
    dict_color_box = {"0" : CONFIGS.COULEURS[0], "1" : CONFIGS.COULEURS[1], "2" : CONFIGS.COULEURS[2],
                  "3" : CONFIGS.COULEURS[3], "4" : CONFIGS.COULEURS[4]}
    
    color = dict_color_box[digit]
  
    turtle.up()
    turtle.goto(CONFIGS.ZONE_PLAN_MINI[0] + (elem*dimention_box[0]), CONFIGS.ZONE_PLAN_MAXI[1] - (line*dimention_box[1]))
    turtle.speed(10)
    turtle.down()
    
    for cote in range(2):
        turtle.tracer(0)
        turtle.begin_fill()
        turtle.color(color)
        turtle.forward(dimention_box[0])
        turtle.right(dimention_box[2])
        turtle.forward(dimention_box[1])
        turtle.right(dimention_box[2])
        turtle.end_fill()
    
def hide_dot():
    if CONFIGS.POSITION_DEPART == [-1, 1]:
        digit = 0
        color = CONFIGS.COULEURS[int(digit)]
    else:
        digit = CONFIGS.map[CONFIGS.POSITION_DEPART[0]][CONFIGS.POSITION_DEPART[1]]
        #print(digit)
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
    event()



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
    event()


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
    event()


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
    event()



def event():
    print(CONFIGS.objet)
    for elem in CONFIGS.objet:
        print(CONFIGS.objet[elem])
        if CONFIGS.POSITION_DEPART == [int(elem[0]), int(elem[1])]:
            turtle.up()
            turtle.goto(CONFIGS.POINT_AFFICHAGE_INVENTAIRE[0], CONFIGS.POINT_AFFICHAGE_INVENTAIRE[1])
            turtle.down()
            turtle.dot(10, "red")
            turtle.fd(10)
            turtle.write(elem[2])
            
            


def creer_dictionnaire_des_objets(fichier_des_objets):
    file_objets= open(fichier_des_objets, "r", encoding="utf-8")
    file_objets = file_objets.readlines()
    ret_objets = {}
    
    for objet in file_objets:
        for elem in objet:
            objet = objet.replace(" ", "").replace("\n", "").replace("(", "").replace(")", "").replace("\"", "\'")
        
        
        
        print(objet)
        objet = objet.split(",")
        ret_objets[(objet[0], objet[1])] = objet[2]
    print(ret_objets)
    return ret_objets
    
    
  
if __name__ == "__main__":
    turtle.listen()   
    file = CONFIGS.fichier_plan
    CONFIGS.map = file_handling(file)
    #CONFIGS.objet = creer_dictionnaire_des_objets(CONFIGS.fichier_objets)
    #print(CONFIGS.map)
    build_map()
    move()
    
    
    


