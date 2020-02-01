class fichaInvalida(Exception):
    pass



def fichamove(ficha,tomove,interfaz,player):

    if player == "n":
        xpos = int(ficha[0])
        ypos = int( convert(ficha[2].lower()) )
        if interfaz[xpos][ypos] != "n":
            raise fichaInvalida("Invalid tab")


        if tomove.upper() == "L":
            xnew = xpos-1
            ynew = ypos-1 
        elif tomove.upper() == "R":
            xnew = xpos-1
            ynew = ypos+1
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
            "e":6,
            "g":7,
            "h":8,
            
             1:"a",
             2:"b",
             3:"c",
             4:"d",
             5:"e",
             6:"f",
             7:"g",
             8:"h"
    }

    return switcher[string]

def vlibre(fichas):
    for i in range(1, len(fichas["n"])  ):
        if fichas["n"][i][0][0]-1 != fichas["b"][i][0][0]  and  fichas["n"][i][0][1]-1 != fichas["b"][i][0][1]:
            fichas["n"][i][1]=True        
        return  fichas   #["n"][i][0][0]-1,  fichas["n"][i][0][1]-1
    


def poss(lista):
    """ Busca todas las posiciones de las fichas blancas y negras del tablero"""
    listapos =   {  "n":[],  "b":[]  }  
    for i in range(1,8):
        for j in range(1,8):
            if lista[i][j] == "n":
                listapos["n"].append( [(i+1,j),False] )
            elif lista[i][j] == "b":
                listapos["b"].append( [(i+1,j),False] )
    return listapos

