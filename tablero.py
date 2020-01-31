class tablero:

    def vista(self,lista):
        tabla = "     a  b  c  d  e  f  g  h \n"
        for vertical in range(len(lista)):
            for i in range(0,10):
                tabla += "  "+lista[vertical][i]
            
        return tabla



    def crearTablero(self):

        tabla = []
        for i in range(1,9):
            tabla.append([str(i),".",".",".",".",".",".",".",".","\n"])
        return tabla



    def lisInit(self,simbol,startList,start,end,step,row):
        for i in range(start,end,step):
            startList[row][i] = str(simbol)
        
        return startList





