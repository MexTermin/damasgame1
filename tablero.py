class tablero:

    def vista(self,lista):
        # se encarga de crear la vista del tablero
        # convierte la matriz en una string y la divide por partes
        tabla = "     a  b  c  d  e  f  g  h \n"
        for vertical in range(len(lista)):
            for i in range(10):
                tabla += "  "+lista[vertical][i]
            
        return tabla


    def crearTablero(self):
        # Se encarga de crear el tablero principal
        tabla = []
        for i in range(1,9):
            tabla.append([str(i),".",".",".",".",".",".",".",".","\n"])
        return tabla


    def lisInit(self,simbol,startList,start,row):
        # crear la posicion de las fichas iniciales
        for i in range(start,9,2):
            startList[row][i] = str(simbol)
        
        return startList





