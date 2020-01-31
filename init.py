from tablero import *

table = tablero()
global mesa


interfaz = table.crearTablero()
interfaz = table.lisInit("B",interfaz,1,9,2,0)
interfaz = table.lisInit("B",interfaz,0,9,2,1)
interfaz = table.lisInit("B",interfaz,1,9,2,2)


interfaz = table.lisInit("N",interfaz,1,9,2,5)
interfaz = table.lisInit("N",interfaz,0,9,2,6)
interfaz = table.lisInit("N",interfaz,1,9,2,7)


mesa = table.vista(interfaz)

print(mesa)
