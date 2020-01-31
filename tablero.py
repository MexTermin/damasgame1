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



    def lisInit(self,startList):
        # ver=1
        # for j in range(0,3):
           
        #     for i in range(1,8,2):
                
        #         startList[j][ver] = "D"
        #         ver+=2
        #     ver=0

        # ver=1
        # hor=0
        # while True:
        #     startList[hor][ver] = "D"
        #     if hor == 3:
        #         break
        #     ver +=2
  
        #     if ver >=8 :
        #         hor += 1
        #         ver = 2

        
        return startList





