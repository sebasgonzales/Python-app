#auto (TAD SIMPLE)
def Crearauto(): 
    auto=[["","",0],["",0]]
    return auto
#----------------------------------------------------------------PENSAR COMO MATRIZ--------------------------------------
def CargarIngreso(auto,patente,hora_ingreso,torre): 
    auto[0][0]=patente
    auto[0][1]=hora_ingreso
    auto[0][2]=torre

def CargarSalida(auto,hora_salida,montototal): 
    auto[1][0]=hora_salida
    auto[1][1]=montototal
 
#-------------------------------------------------------------------------------------------------------
def VerPatente(auto): 
    return auto[0][0]

def VerHoraIngreso(auto):
    return auto[0][1]

def VerTorre(auto):
    return auto[0][2]

def VerHoraSalida(auto):
    return auto[1][0]

def VerMontoTotal(auto):
    return auto[1][1]

#--------------------------------------------------------------------------------------------------------
def ModificarPatente(auto,auto2): 
    auto[0][0]=auto2

def ModificarHoraIngreso(auto,auto2):
    auto[0][1]=auto2

def ModificarTorre(auto,auto2):
    auto[0][2]=auto2

def ModificarHoraSalida(auto,auto2):
    auto[1][0]=auto2

def ModificarMontoTotal(auto,auto2):
    auto[1][1]=auto2

#--------------------------------------------------------------------------------------------------------
def Asignarauto(auto,auto2): 
    ModificarPatente(auto,VerPatente(auto2))
    ModificarHoraIngreso(auto,VerHoraIngreso(auto2))
    ModificarTorre(auto,VerTorre(auto2))
    ModificarHoraSalida(auto,VerHoraSalida(auto2))
    ModificarMontoTotal(auto,VerMontoTotal(auto2))
  