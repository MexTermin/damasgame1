# genera una excetion cuando ponen la hubiccion de una ficha invalida
class fichaInvalida(Exception):
    pass
class movinvalido(Exception):
    pass

def fichamove(ficha,tomove,interfaz,player):

    if player == "n":
        xpos = int(ficha[0])
        ypos = int( convert(ficha[2].lower()) )
        if interfaz[xpos][ypos] != "n":
            raise fichaInvalida("Invalid tab")
        if tomove.upper() == "L":
            if vlibre((xpos,ypos),interfaz) == "left" or  vlibre((xpos,ypos),interfaz) == "bot":
                xnew = xpos-1
                ynew = ypos-1 
            else:
                raise movinvalido("Esta ficha no se puede mover al left")
        elif tomove.upper() == "R":
            if vlibre((xpos,ypos),interfaz) == "right" or vlibre((xpos,ypos),interfaz) == "bot":
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
        xpos = int(ficha[0])
        ypos = int( convert(ficha[2].lower()) )
        if interfaz[xpos][ypos] != "b":
            raise fichaInvalida("Invalid tab")
        if tomove.upper() == "L":
            xnew = xpos+1
            ynew = ypos-1 
        elif tomove.upper() == "R":
            xnew = xpos+1
            ynew = ypos+1
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
            
            #  1:"a",
            #  2:"b",
            #  3:"c",
            #  4:"d",
            #  5:"e",
            #  6:"f",
            #  7:"g",
            #  8:"h"
    }

    return switcher[string]

def vlibre(ficha,interfaz):
    left=False
    right=False
    if interfaz[ficha[0]][ficha[1]] =="n":
        if interfaz[ficha[0]-1][ficha[1]-1] != "n" and interfaz[ficha[0]-1][ficha[1]-1] != "b":
            left = True

        if interfaz[ficha[0]-1][ficha[1]+1] != "n" and interfaz[ficha[0]-1][ficha[1]+1] != "b":
            right = True
    if left == True and right == True:
        return "bot"
    elif left == True and right == False:
        return "left"
    elif right == True:
        return "right"
    else:
        return False

    # for first in range(0, len(fichas["n"])  ):
    #     for second in range(len(fichas["b"])):
    #         if fichas["n"][first][0][0]-1 != fichas["b"][second][0][0]  and  fichas["n"][first][0][1]-1 != fichas["b"][second][0][1]:
    #             fichas["n"][first][1]=True       
    #return  fichas   #["n"][i][0][0]-1,  fichas["n"][i][0][1]-1
    


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

