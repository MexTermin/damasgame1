# genera una excetion cuando ponen la hubiccion de una ficha invalida
class fichaInvalida(Exception):
    pass
class movinvalido(Exception):
    pass

def fichamove(ficha,tomove,interfaz,player):
    xpos = int(ficha[0])
    ypos = int( convert(ficha[2].lower()) )
    if player == "n":
        if interfaz[xpos][ypos] != "n":
            raise fichaInvalida("Invalid tab")
        if tomove.upper() == "L":
            if vlibre((xpos,ypos),interfaz,player) == "left" or  vlibre((xpos,ypos),interfaz,player) == "bot":
                xnew = xpos-1
                ynew = ypos-1 
            else:
                raise movinvalido("Esta ficha no se puede mover al left")
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
    return interfaz,player
    

def convert(string):
    """ regresa el valor de la conversion de los numero en str y los str en num """
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
        if interfaz[ficha[0]] [ficha[1]] =="n":
            x1,y1,x2,y2=-1,-1,-1,1
        else:
            return False
    if player == "b":
        #--------------------------------------------------
        if interfaz[ficha[0]] [ficha[1]] =="b":
            x1,y1,x2,y2=1,-1,1,1
        else:
            return False       
    #-------------------------------------------------------------------------------------------- 
    #  Revisamos si la ficha tiene libre la derecha y la izquierda
    if interfaz[ficha[0]+x1] [ficha[1]+y1] != "n" and interfaz[ficha[0]+x1] [ficha[1]+y1] != "b":
        left = True
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


def poss(lista):
    """ Busca todas las posiciones de las fichas blancas y negras del tablero"""
    listapos =   {  "n":[],  "b":[]  }  
    for i in range(9):

        for j in range(9):

            if lista[i][j] == "n":
                listapos["n"].append( (i,j) )

            elif lista[i][j] == "b":
                listapos["b"].append( (i,j) )

    return listapos

