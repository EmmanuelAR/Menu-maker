import random
import DB
import Clases

haySpaghetti = False
hayPescado = False
haySopa = False

def valor_repetido(array, valor):
    return array.count(valor) >= 1 

def getValorSinRepetir(listaBase,listaFinal):
  valido = False
  while valido == False:
    valor = random.choice(listaBase)
    if valor_repetido(listaFinal,valor) == True:
      valido=False
    else:
      valido=True
  return valor


def objeto_repetido(array, objeto):
    contador = 0
    for elemento in array:
        if elemento == objeto:
            contador += 1
    if contador >= 1:
        return True
    else:
        return False

def premiumRules(valor,day):
  global hayPescado
  if (valor.status == 'Premium' and day.type != 'Premium') or (valor.status != 'Premium' and day.type == 'Premium'):
    return False
  else:
    if ((valor.status == 'Premium' and day.type == 'Premium') and (hayPescado == True and valor.type =='Pescado')):
      return False
    if valor.type == 'Pescado':
      hayPescado=True
      return True

def reglas_sopa_spaguetti(valor):
  global haySopa
  global haySpaghetti
  if(haySopa == True and valor.type =='Sopa') or (haySpaghetti == True and valor.type =='Spaghetti'):
    return False
  else:
      if valor.type == 'Sopa':
        haySopa=True
        return True
      
      if valor.type == 'Spaghetti':
        haySpaghetti=True
        return True

def validar_reglas(valor,day):

  if objeto_repetido(DB.listaFinalLuchNames,valor.descp) == True:
    return False
  else:
    if premiumRules(valor,day) == False:
      return False
    else:
      if reglas_sopa_spaguetti(valor) == False:
        return False
      else:
        return True

def getlunch(day):
  valido = False
  while valido == False:
    valor = random.choice(DB.lunchList)
    if validar_reglas(valor,day) == True:
      valido=True
    else:
      valido=False
  DB.listaFinalLuchNames.append(valor.descp)
  return valor

def resetVariables():
    DB.listaFinalBreakFast =[]
    DB.listaFinalSnacks =[]
    DB.listaFinalLuchNames =[]
    DB.listaFinalLuchObjs =[]
    lunes= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Lunes','Normal')
    martes= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Martes','Normal')
    miercoles= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Miercoles','Normal')
    jueves= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Jueves','Normal')
    viernes= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Viernes','Normal')
    sabado= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Sabado','Premium')
    DB.days=[lunes,martes,miercoles,jueves,viernes,sabado]