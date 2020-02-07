from tablero import *
from fichas import *
from os import system
table = tablero()
global mesa
global interfaz
jugadores = players()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! optimizar !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

interfaz = table.crearTablero()
interfaz = table.lisInit("b",interfaz,1,1)
interfaz = table.lisInit("b",interfaz,2,2)
interfaz = table.lisInit("b",interfaz,1,3)

interfaz = table.lisInit("n",interfaz,2,6)
interfaz = table.lisInit("n",interfaz,1,7)
interfaz = table.lisInit("n",interfaz,2,8)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def start():
    global mesa
    global interfaz
    #system("cls")
    if jugadores.player1 == "":
        letter = input("jugdor 1, ¿deseas ser n o b ? ")
        if letter.lower() == "n":
            jugadores.player1="n"
            jugadores.turno="n"
            jugadores.player2="b"
        elif letter.lower() == "b":
            jugadores.player1="b"
            jugadores.turno="b"
            jugadores.player2="n"
        else:
            #system("cls")
            input("Cabron te dije que elijas n o r, press enter to continue... ")
            start()
    mesa = table.vista(interfaz)

    #system("cls")
    print("Es el turno de las fichas ",jugadores.turno)
    print(mesa)
    
    meal = obligatoryEat(interfaz,jugadores.turno)
    if meal[0] != False:
        if len(meal) == 1:
            input( "You should eat the right down tab {} '{}' ".format(meal[0][1], meal[0][0] ) )
            interfaz, jugadores.turno = eat(meal[0][1],interfaz,meal[0][0],jugadores.turno)
        else:
            print(meal)
            for i in range( len(meal) ):
                print(i,"  ",end = "") 
            try:

                answer = int(input("Select your answer: "))
            except :
                print("Tenes que elegir un numero del 0 al ", len(meal))
            interfaz, jugadores.turno = eat(meal[answer][1],interfaz,meal[answer][0],jugadores.turno)

    else:
        num = input("ingresa la ficha que deseas mover seguido de L (left) o R (right): ")
        num = num.split(" ")
        try:
            interfaz,jugadores.turno = fichamove( num[0], num[1] ,interfaz  ,jugadores.turno ) 
        except fichaInvalida as e:
            system("cls")
            input(str(e))
        except movinvalido as e:
                input(str(e))
        # except:
        #     system("cls")
        #     input("debes ingresar la posicion de la ficha y luego a donde ira, ejemplo '6,B L'")


    start()
    

start()