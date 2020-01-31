from tablero import *

table = tablero()
global mesa


interfaz = table.crearTablero()
interfaz = table.lisInit(interfaz)

mesa = table.vista(interfaz)

print(mesa)
