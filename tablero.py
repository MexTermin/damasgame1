from coloreshell import *
class tablero:

    def vista(self,lista):
        # se encarga de crear la vista del tablero
        # convierte la matriz en una string y la divide por partes
        indicator = 0
        colour = 0
        pos = ""
        tabla = "  a  b  c  d  e  f  g  h "
        for vertical in range(1,len(lista)):
            colour = 0 if  (indicator == 1) else 1
            tabla+="\n" + str(vertical)
            for i in range(1,9):
                c = Colour.BLACK if (colour ==0) else Colour.WHITE1
                pos =   "   "  if (lista[vertical][i]  ==   ".")  else " "   +   str(lista[vertical][i])  +   " "
                tabla += c +  pos +  Colour.END
                colour = 1  if (colour == 0) else  0 
            indicator = 1 if  (indicator == 0) else 0
            
        return tabla


    def crearTablero(self):
        # Se encarga de crear el tablero principal
        tabla = []
        for i in range(9):
            tabla.append([".",".",".",".",".",".",".",".","."])
        return tabla


    def lisInit(self,simbol,startList,start,row):
        # crear la posicion de las fichas iniciales
        for i in range(start,9,2):
            startList[row][i] = str(simbol)
        
        return startList

class players:
    def __init__(self):
        self.player1=""
        self.player2=""
        self.turno="n"


        





