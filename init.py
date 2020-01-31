from tablero import *
from fichas import *

table = tablero()
global mesa


interfaz = table.crearTablero()
interfaz = table.lisInit("b",interfaz,1,0)
interfaz = table.lisInit("b",interfaz,2,1)
interfaz = table.lisInit("b",interfaz,1,2)


interfaz = table.lisInit("n",interfaz,1,5)
interfaz = table.lisInit("n",interfaz,2,6)
interfaz = table.lisInit("n",interfaz,1,7)
posicion = poss(interfaz)
print(vlibre(posicion))
mesa = table.vista(interfaz)

def start



print(mesa)
