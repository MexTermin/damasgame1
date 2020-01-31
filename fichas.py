def fichamove():
    pass

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
    for i in range( len(fichas["n"])  ):
        if fichas["n"][i][0][0]-1 != fichas["b"][i][0][0]  and  fichas["n"][i][0][1]-1 != fichas["b"][i][0][1]:
            fichas["n"][i][1]=True
            
        return  fichas
    


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

