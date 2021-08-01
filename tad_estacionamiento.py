def Crearestacionamiento():
    estacionamiento=[]
    return estacionamiento
#---------------------------------------------------
def AgregarA(estacionamiento,a):
    estacionamiento.append(a)
#---------------------------------------------------
def EliminarA(estacionamiento,a):
    estacionamiento.remove(a)
#---------------------------------------------------
def RecuperarAuto(estacionamiento,i): 
    return estacionamiento[i]
#---------------------------------------------------
def Tamanio(estacionamiento): 
    return len(estacionamiento)
#---------------------------------------------------
def ExisteA(estacionamiento,a): 
    return a in estacionamiento