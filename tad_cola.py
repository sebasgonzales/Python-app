def CrearCola(): #retorna cola vacia
    c=[]
    return c
#--------------------------------------
def Encolar(c,elemento): #agrega elemento
    c.append(elemento)
#--------------------------------------
def Desencolar(c): #elimina el primer elemento
    elemento=c.pop(0)
    return elemento
#--------------------------------------
def ColaVacia(c): #True o False si tiene elementos
    if c==[]:
        return True
    else:
        return False
#--------------------------------------
def copiarCola(cola1,cola2):
   aux=CrearCola() 
   while not ColaVacia(cola2):
        elem=Desencolar(cola2)
        Encolar(aux,elem) 
   while not ColaVacia(aux):
        elem=Desencolar(aux)
        Encolar(cola1,elem)
        Encolar(cola2,elem)
