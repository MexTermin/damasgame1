from tablero import *
from fichas import *

table = tablero()
global mesa
global interfaz
interfaz = table.crearTablero()
interfaz = table.lisInit("b",interfaz,1,0)
interfaz = table.lisInit("b",interfaz,2,1)
interfaz = table.lisInit("b",interfaz,1,2)

interfaz = table.lisInit("n",interfaz,1,5)
interfaz = table.lisInit("n",interfaz,2,6)
interfaz = table.lisInit("n",interfaz,1,7)



def start():
    global mesa
    global interfaz
    mesa = table.vista(interfaz)
    print(mesa)
    num = input("ingresa la ficha que seas mover y su ubicacion: ")
    num = num.split(" ")
    interfaz = fichamove( num[0], num[1] ,interfaz  ,"n" ) 
    start()

start()