#TRABAJO PRACTICO INTEGRADOR, EJERCICIO 7.
#GONZALES TELLO, Sebastian.
#CANGARO, Ignacio Gabriel.
#PONCE, Lucas Ponce.


#En la ciudad de Buenos Aires, un conjunto de oficinas poseen un estacionamiento para los
#trabajadores y para los clientes de dicho lugar. Al momento de ingresar un vehiculo, se necesita
#almacenar su patente, la hora de ingreso y ademas se almacena la torre a la cual entra la persona.
#Cuando un vehiculo deja el estacionamiento, se almacena la hora de salida y el monto total de la
#estadía. Se realizará un descuento del 15% a todos los vehiculos que hayan estado en la torre 3. El
#valor de la hora de estadía se define al iniciar el día. Se deberá desarrollar una aplicación,
#utilizando los TADs que crea necesarios. Se desea tener un menú con los siguientes puntos:
#a) Ingresar vehículo
#b) Modificar vehículo
#c) Registrar salida de vehículo
#d) Listado de vehículos
#e) Generar informe indicando el monto recaudado por cada torre
#f) Cantidad de vehiculos ingresados en las horas pico (7hs hasta las 10hs/17hs hasta las 20hs)
#g) Eliminar los vehículos que ingresaron luego de las 18 hs a una torre determinada
#h) Generar una cola con los vehículos de una torre determinada.


from tad_cola import*   #Importo el tad_cola 
from tad_estacionamiento import*    #Importo el tad_estacionamiento    
from tad_auto import*       #Importo el tad_auto
from datetime import*       #Importo librerias del datetime
from os import system 
from datetime import date #LIBRERIAS PARA LAS OPERACIONES CON TIPO DATO -> FECHA
from datetime import datetime   #



estacionamiento=Crearestacionamiento()      #Creo un vector vacío mediante el "Crearestacionamiento"  


canttorres=int(input("Ingrese la cantidad de torres del estacionamiento: "))

horaestadia=float(input("Ingrese el precio de la hora del estacionamiento: $ "))

continuar=1     #Esta variable permite mantener el menú utilizando el while
while(continuar==1):    #While que abarca todo el menú de operaciones posibles con el programa
    system('cls')       #Limpiar pantalla
    print("✺✺✺✺✺✺✺  Bienvenido,seleccione una de las opciones  ✺✺✺✺✺✺✺")
    print("\n")
    print("1) Ingresar vehículo")
    print("2) Modificar vehículo")
    print("3) Registrar salida de vehículo")
    print("4) Listado de vehículos")
    print("5) Generar informe indicando el monto recaudado por cada torre")
    print("6) Cantidad de vehiculos ingresados en las horas pico (7hs hasta las 10hs/17hs hasta las 20hs)")
    print("7) Eliminar los vehículos que ingresaron luego de las 18 hs a una torre determinada")
    print("8) Generar una cola con los vehículos de una torre determinada.")
    print("9) SALIR")
    print("\n")
    eleccion=input("Ingrese una opcion:")   #Lo que ingrese el usuario será de tipo entero y se almacenará en la variable "eleccion"

    if(eleccion=="1"):          
        system('cls')
        auto=Crearauto()        #Se crea una matriz de auto completamente vacía mediante la función "Crearauto"
        patente=input("Ingrese el numero de la patente(SIN ESPACIOS): ")    #Se empieza a llenar la matriz con datos del usuario
        hora_ingreso=input("Ingrese hora de ingreso al estacionamiento en formato (hh:mm:ss): ")
        torre=int(input("Ingrese la torre a la cual ingresa el auto : "))
        while (torre<=0 or torre>canttorres):       #Permite establecer un límite en el que el usuario no pueda asignar una torre inexistente al auto a ingresar
            print("La torre ingresada no existe, por favor vuelva a intentarlo")
            print("\n")
            input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")
            system('cls')
            torre=int(input("Ingrese la torre a la cual ingresa el auto : "))
        CargarIngreso(auto,patente,hora_ingreso,torre) #Se cargan los datos del auto ingresados por el usuario
        AgregarA(estacionamiento,auto)      #Se agrega el auto al estacionamiento creado al principio del código
    
    
    elif(eleccion=="2"):
        system('cls')
        bandera=0       #Permite saber si la patente del auto a modificar es correcta
        numeropatente=input("Ingrese el numero de la patente a modificar(SIN ESPACIOS): ") #Se ingresa la patente que se desea modificar
        for i in range(Tamanio(estacionamiento)):   #Una iteración que se repite la cantidad de autos que tenga el vector estacionamiento
            auto=RecuperarAuto(estacionamiento,i)   #Se recuperan los datos del auto cargados en el vector estacionamiento
            if(VerPatente(auto)==numeropatente):    #Latente ingresada debe coincidir con alguna patente de auto cargada anteriormente
                bandera=1                           #Indica que la patente fue encontrada
                automodificado=Crearauto()          #Se crea un nuevo auto vacío con los nuevos datos a modificar
                patente=input("Ingrese el nuevo numero de la patente(SIN ESPACIOS): ")
                hora_ingreso=input("Ingrese la nueva hora de ingreso al estacionamiento en formato (hh:mm:ss): ")
                torre=int(input("Ingrese la nueva  torre a la cual entro  : "))
                while (torre<=0 or torre>canttorres):       #Permite establecer un límite en el que el usuario no pueda asignar una torre inexistente al auto a ingresar
                 print("La torre ingresada no existe, por favor vuelva a intentarlo")
                 print("\n")
                 input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")
                 system('cls')
                 torre=int(input("Ingrese la torre a la cual ingresa el auto : "))
                CargarIngreso(automodificado,patente,hora_ingreso,torre)    #Se cargan los datos del automodificado ingresados por el usuario
                Asignarauto(auto,automodificado)        #Se reemplaza todo lo que se ingresó al automodificado en auto, para que se pueda 
                break
        if(bandera==0):         #En este caso, la patente es incorrecta
            print(" VEHICULO NO REGISTRADO, POR FAVOR REVISE LA PATENTE INGRESADA ")
            print("\n")
            input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")



    elif(eleccion=="3"):
        system('cls')
        bandera=0 #Permite saber si la patente del auto a registrar salida es correcta
        numeropatente=input("Ingrese el numero de la patente(SIN ESPACIOS): ")
        for i in range(Tamanio(estacionamiento)):
            autorec=RecuperarAuto(estacionamiento,i)    #Se recupera el auto completo en una variable
            hora_ingreso=VerHoraIngreso(autorec)        #Se almacena la hora de ingreso en una variable a parte que no va a ser modificada
            if(VerPatente(autorec)==numeropatente):
                bandera=1       #Indica que la patente fue encontrada
                hora_salida=input("Ingrese hora de salida del estacionamiento en formato (hh:mm:ss): ") #El usuario indica la hora de salida del auto
                formato = "%H:%M:%S" #El formato en el que utiliza el datetime para poder realizar la diferencia
                diferencia= (datetime.strptime(hora_salida, formato) - datetime.strptime(hora_ingreso, formato)).seconds  #Se realiza una diferencia entre la hora de salida y la hora de ingreso con resultados en segundos
                monto=((diferencia/3600)*horaestadia)   #Se guarda en la variable la operación necesaria para obetener el monto total del vehículo a salir
                if(VerTorre(autorec)==3):       #Si el auto recuperado se encuentra en la torre 3, se le aplicará un descuento
                    monto_total=(monto-(monto*0.15))    #Variable para el monto con descuento
                    CargarSalida(autorec,hora_salida,monto_total)   #Se carga en la matriz del auto su hora de salida y el monto total pagado
                else:                           #Sino aplica a la torre 3, no hay descuento y carga los datos con normalidad
                    monto_total=monto
                    CargarSalida(autorec,hora_salida,monto_total)
        if(bandera==0):   # Al no encontrarse el auto imprime un mensaje y deja volver al menu 
            print(" VEHICULO NO REGISTRADO, POR FAVOR REVISE LA PATENTE INGRESADA ")
            print("\n")
            input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")

    elif(eleccion=="4"):
        system('cls')
        if(Tamanio(estacionamiento)!=0):  # Si hay autos en el estacionamiento, se recorre con una iteración.  
            print("\n")
            print("✇  ¤¤¤ 🅅 🄴 🄷 🄸 🄲 🅄 🄻 🄾 🅂 ¤¤¤  ✇")
            print("\n")
            for i in range(Tamanio(estacionamiento)):
                auto=RecuperarAuto(estacionamiento,i)
                print("\n")
                print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
                print("PATENTE : ",VerPatente(auto))     #Se visualiza la posición de la matriz en la que encuentra la patente
                print("\n")  
                print("HORA DE INGRESO : ",VerHoraIngreso(auto))   #Se visualiza la posición de la matriz en la que encuentra la hora de ingreso
                
                print("NUMERO DE TORRE : ",VerTorre(auto))      #Se visualiza la posición de la matriz en la que encuentra la torre
                
                if (VerMontoTotal(auto) > 0 ):                 # Solamente si el auto tiene algo que pagar (osea que ya se registro su salida) listamos tambien estos datos 
                 print("HORA DE SALIDA : ",VerHoraSalida(auto)) #Se visualiza la posición de la matriz en la que encuentra la hora de salida
                
                 

                 print("MONTO A PAGAR : $",'%.2f' % VerMontoTotal(auto))  #Se visualiza la posición de la matriz en la que encuentra el monto total
                
                print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")     
        else:
            print("NINGUN VEHICULO HA SIDO REGISTRADO HASTA EL MOMENTO")
            print("\n")
            input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")
        input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")
    


    elif(eleccion=="5"):
        
        system('cls')
        print("$$$$$$$$$$$$$$$$$$$$$$$$ DINERO RECAUDADO $$$$$$$$$$$$$$$$$$$$$$$$") 
        print("\n")
        for i in range(canttorres):
            acumulador=0
            for j in range(Tamanio(estacionamiento)):  #Recorro el estacionamiento  POR TORRE para sumar con el acumulador, el dinero 
                auto=RecuperarAuto(estacionamiento,j)  # recaudado por cada una de ellas.
                torre=VerTorre(auto)
                torre=torre-1
                if(torre==i):
                    acumulador=acumulador+VerMontoTotal(auto)
         
            print("            El monto total de la torre {} es: ${} ".format(i+1,'%.2f' %acumulador))   
        print("\n") 
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")    
        print("\n") 
        input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")

    elif(eleccion=="6"):
        system('cls')
        if(Tamanio(estacionamiento)!=0):        #Mientras el estacionamiento no este vacio, sucedera lo siguiente:
            contador=0
            for i in range(Tamanio(estacionamiento)):
                autorec=RecuperarAuto(estacionamiento,i)                        #Recupero los datos del auto, para luego comparar la hora.
                format = '%H:%M:%S'
                hora_ingreso=datetime.strptime(VerHoraIngreso(autorec), format) #Creo variables con las horas a evaluar, para luego compararlas
                horario1a=datetime.strptime("07:00:00", format)                 #entre si, para poder especificar que cantidad de autos entraron en
                horario1b=datetime.strptime("10:00:00", format)                 #horas pico.
                horario2a=datetime.strptime("17:00:00", format)
                horario2b=datetime.strptime("20:00:00", format)
                if((hora_ingreso >= horario1a and hora_ingreso <= horario1b) or (hora_ingreso >= horario2a and hora_ingreso <= horario2b)):
                    contador+=1                                                 #Comparo las horas, y sumo al contador cuando la condicion se cumpla.
        
            print(" LA CANTIDAD DE VEHICULOS INGRESADOS EN LAS HORAS PICO ES DE : {} ".format(contador))
            print("\n")
            input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")
        else:
            print("NINGUN VEHICULO HA SIDO REGISTRADO HASTA EL MOMENTO")
            print("\n")
            input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")


    elif(eleccion=="7"):
        system('cls')
        numerodetorre=int(input("Ingrese el numero de la torre : "))
        i=0
        if (numerodetorre<=0 or numerodetorre>canttorres):                       #Sucesion para verificar si la torre existe
         print("La torre ingresada no existe, por favor vuelva a intentarlo")
         print("\n")
         input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")
         system('cls')
         numerodetorre=int(input("Ingrese el numero de la torre : "))
        else:
            for i in range(Tamanio(estacionamiento)):  #Recorremos el estacionamiento recuperando los datos para tener la hora de ingreso 
                i=0
                auto=RecuperarAuto(estacionamiento,i)
                torre=VerTorre(auto)
                if(VerTorre(auto)==numerodetorre):
                    format = "%H:%M:%S"
                    hora_ingreso=datetime.strptime(VerHoraIngreso(auto), format)
                    horario=datetime.strptime("18:00:00", format) #Creo una variable de valor "18:00:00"
                    if(hora_ingreso >= horario):
                        EliminarA(estacionamiento,auto)           #Si la hora a la que ingreso es mayor o igual al horario que definimos, se elimina el auto de la lista del estacionamiento.

                    else:   
                        print("No hay autos en el estacionamiento despues de esa hora")
                        print("\n")
                        input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")

                       
    elif(eleccion=="8"):
        system('cls')
        numerodetorre=int(input("Ingrese el numero de la torre : "))    #Pedimos que se ingrese la torre de la cual se quieren encolar los autos.
        while (numerodetorre<=0 or numerodetorre>canttorres):           #Misma sucesion que antes, para verificar si la torre existe.
         print("La torre ingresada no existe, por favor vuelva a intentarlo")
         print("\n")
         input("                                                                                    . . . PULSE ENTER PARA CONTINUAR . . .")
         system('cls')
         numerodetorre=int(input("Ingrese el numero de la torre : "))
        if(Tamanio(estacionamiento) != 0):                             #Mientras el estacionamiento no este vacio, sucedera:
            vehiculosentorre=CrearCola()    #Creo una cola vacía
            i=numerodetorre
            print("\n")
            print("\n")
            print("\n")
            print("Ingresando autos de la torre {} a la cola... ".format(i))  
            for i in range(Tamanio(estacionamiento)):
                auto=RecuperarAuto(estacionamiento,i)              #Recupero los datos de los autos

                if(VerTorre(auto)==numerodetorre):                 #Si la torre que se recupero antes, es igual a la torre que se ingreso, el auto es encolado.
                    Encolar(vehiculosentorre,auto)   
        else:
            print("No hay autos en el estacionamiento de esa torre.")
        j=0
        for j in range(Tamanio(vehiculosentorre)):
                auto=RecuperarAuto(vehiculosentorre,j)
                print("\n")
                print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")                  #Como en el punto 4, listo los autos que estan en la cola.
                print("PATENTE : ",VerPatente(auto))
                print("\n")
                print("HORA DE INGRESO : ",VerHoraIngreso(auto))
                
                print("NUMERO DE TORRE : ",VerTorre(auto))
                
                if (VerMontoTotal(auto) > 0 ):
                 print("HORA DE SALIDA : ",VerHoraSalida(auto))
                
                 

                 print("MONTO A PAGAR : $",'%.2f' % VerMontoTotal(auto))
                
                print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")     
        input()
    
    elif(eleccion=="9"):
        continuar=0     #Finaliza el programa

