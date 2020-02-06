# genera una excetion cuando ponen la hubiccion de una ficha invalida
class fichaInvalida(Exception):
    pass
class movinvalido(Exception):
    pass

def fichamove(ficha,tomove,interfaz,player):
    xpos = int(ficha[0])
    ypos = int( convert(ficha[2].lower()) )
    print("\nLa  posicion de fichas es, ", (xpos,ypos))
    if player == "n":
        if interfaz[xpos][ypos] != "n":
            raise fichaInvalida("Invalid tab")
        if tomove.upper() == "L":
            if vlibre((xpos,ypos),interfaz,player) == "left" or  vlibre((xpos,ypos),interfaz,player) == "bot":
                xnew = xpos-1
                ynew = ypos-1 
            else:
                raise movinvalido("Esta ficha nos se puede mover al left")
        elif tomove.upper() == "R":
            if vlibre((xpos,ypos),interfaz,player) == "right" or vlibre((xpos,ypos),interfaz,player) == "bot":
                xnew = xpos-1
                ynew = ypos+1
            else:
                raise movinvalido("Esta ficha no se puede mover al right")
        else:
            return "Invalid move"
        interfaz[xpos][ypos] = "."
        interfaz[xnew][ynew] = "n"
        print("\nSe movio a la posicion, ", (xnew,ynew))
        player="b"

    elif player == "b":
            if interfaz[xpos][ypos] != "b":
                raise fichaInvalida("Invalid tab")
            if tomove.upper() == "L":
                if vlibre((xpos,ypos),interfaz,player) == "left" or  vlibre((xpos,ypos),interfaz,player) == "bot":
                    xnew = xpos+1
                    ynew = ypos-1 
                else:
                    raise movinvalido("Esta ficha no se puede mover al left")
            elif tomove.upper() == "R":
                if vlibre((xpos,ypos),interfaz,player) == "right" or vlibre((xpos,ypos),interfaz,player) == "bot":
                    xnew = xpos+1
                    ynew = ypos+1
                else:
                    raise movinvalido("Esta ficha no se puede mover al right")
            else:
                return "Invalid move"
            interfaz[xpos][ypos] = "."
            interfaz[xnew][ynew] = "b"
            player="n"
            print("\nSe movio a la posicion, ", (xnew,ynew))
    return interfaz,player
    
def convert(string):
    """ regresa el valor de la conversion de los numero en str y los str en num """
    string = string.lower()
    switcher =  {
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8,

    }

    return switcher[string]

def vlibre(ficha,interfaz, player):
    left=False
    right=False
    # asignamos los valores que comparan si esta libre el camino segun sean para las fichas N o B
    if player == "n":
        # validamos si la ficha elegida pertenece al jugador
        if interfaz[int(ficha[0])] [int(ficha[1])] =="n":
            x1,y1,x2,y2=-1,-1,-1,1
        else:
            return False
    if player == "b":
        #--------------------------------------------------
        if interfaz[int(ficha[0])] [int(ficha[1])] =="b":
            x1,y1,x2,y2=1,-1,1,1
        else:
            return False       
    #-------------------------------------------------------------------------------------------- 
    #  Revisamos si la ficha tiene libre la derecha y la izquierda
    if ficha[0]>1 and ficha[0] >1:
        if interfaz[ficha[0]+x1] [ficha[1]+y1] != "n" and interfaz[ficha[0]+x1] [ficha[1]+y1] != "b":
            left = True
    if ficha[0] <=8 and ficha [1] <8:
        if interfaz[ficha[0]+x2] [ficha[1]+y2] != "n" and interfaz[ficha[0]+x2] [ficha[1]+y2] != "b":
            right = True
    #-------------------------------------------------------------------------------------------
    #Segun los resultados de las pruebas anteriores regresamos cual espacio tiene libre la ficha
    if left == True and right == True:
        return "bot"
    elif left == True and right == False:
        return "left"
    elif right == True:
        return "right"
    else:
        return False

def pos(lista):
    """ Busca todas las posiciones de las fichas blancas y negras del tablero"""
    listapos =   {  "n":[],  "b":[]  }  
    for i in range(9):

        for j in range(9):

            if lista[i][j] == "n":
                listapos["n"].append( (i,j) )

            elif lista[i][j] == "b":
                listapos["b"].append( (i,j) )

    return listapos

def counter(player):
    if player == "n":
        return "b"
    if player == "b":
        return "n"
    else:
        return False

def eat(ficha,interfaz,direction,player):
    #all = poss(interfaz)
    if direction.upper() == "L":
        input("You should eat the left tab {} 'L' ".format((ficha[0],ficha[1])))
        x1,y1,x2,y2 = -1,-1,-2,-2 

    elif direction.upper() == "R":
        input("You should eat the Right tab {} 'R' ".format((ficha[0],ficha[1])))
        x1,y1,x2,y2 = -1,1,-2,2


    elif direction.upper() ==  "LD":
        input("You should eat the left down tab {} 'LD' ".format((ficha[0],ficha[1])))
        x1,y1,x2,y2 = 1,-1,2,-2


    elif direction.upper() == "RD":
        input("You should eat the right down tab {} 'RD' ".format((ficha[0],ficha[1])))
        x1,y1,x2,y2 = 1,1,2,2


    interfaz[ficha[0]] [ficha[1]] = "."
    interfaz[ficha[0]+x1] [ficha[1]+y1] = "."
    interfaz[ficha[0]+x2] [ficha[1]+y2] = player
    print("\nLa ficha esta en, ", (ficha[0],ficha[1]))
    print("\n La ficha se movio y comio en , ", (ficha[0]+x1,ficha[1]+y1))
    print("\n La ficha quedo en la pos, ", (ficha[0]+x2,ficha[1]+y2))    
    return interfaz,counter(player)

def obligatoryEat(interface,player):
    #listing = pos(interface)
    # focus = False
    for values in range(1,9):
        for content in range(1,9):
            if interface[values][content] == player:
                if values  < 7 and content < 7:
                    if interface[values+1][content+1] == counter(interface[values][content]) and interface[values+2][content+2] == ".":
                        #return eat((values+1,content+1),interface,"RD",player), counter(player)
                        return "RD" ,[values,content]

                if  values <8  and content >2:
                    if interface[values+1][content-1] == counter(interface[values][content]) and interface[values+2][content-2] == ".":
                        #return eat((values+1,content-1),interface,"R",player), counter(player)
                        return "LD", [values,content]

                if values <7 and content < 7:
                    if  interface[values-1][content+1] == counter(interface[values][content]) and interface[values-2][content+2] == ".":
                        #return eat((values-1,content-1),interface,"L",player) , counter(player)
                        return "R", [values,content]
                        
                if values >2 and content >2:
                    if interface[values-1][content-1] == counter(interface[values][content]) and interface[values-2][content-2] == ".":
                        #return eat((values-1,content+1),interface,"LD",player)   , counter(player)
                        return "L", [values,content]
            else:
                pass
    return False, False
    
def limites():
    pass




   

