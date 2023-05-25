import random


class lunch:
  def __init__(self, type, descp,status):
    self.type = type
    self.descp = descp
    self.status= status

class mealDay:
  def __init__(self, breakFast, snack,lunch,dinner):
    self.breakFast = breakFast
    self.snack = snack
    self.lunch= lunch
    self.dinner= dinner 

class day:
  def __init__(self, mealDay, dayName,type):
    self.mealDay = mealDay
    self.dayName = dayName
    self.type=type


breakfastList=['Pinto con huevo','Pinto con queso','Huevos con tortilla','Prensadas queso y frijol','Tortilla con queso','Sandwich con jamon','Sandwich con huevo','Tostadas con aguacate y huevo','Omelette']
snacksList=['Batido de banano','Batido de melón','Batido de papaya','Uvas','Manzana picada','Mango picado','Yogurt y granola con una fruta']
lunchList=[]

# CARNE ROJA
lunchList.append(lunch('Carne','Tortas carne/Arroz/Frijoles/Ensalda Verde/Agucate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Bistek encebollado/Arroz/Frijoles/Ensalda Verde/Agucate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Fajitas de carne/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Lentejas con carne desmechada/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Canelones con carne desmechada/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Carne en salsa/Arroz/Frijoles/Caracoles/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Arroz chino/Ensalada Verde','Normal'))
lunchList.append(lunch('Carne','Picadillo arracache con carne/arroz','Normal'))

#Carne blanca
lunchList.append(lunch('Carne','Chifrijo','Premium'))
lunchList.append(lunch('Carne','Garbanzos con cerdo/Escabeche','Normal'))
lunchList.append(lunch('Carne','Chuleta cerdo/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Chuleta ahumada/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Costilla cerdo frita/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Carne','Frijoles blancos con cerdo/Escabeche','Normal'))
lunchList.append(lunch('Carne','Frijoles tiernos con cerdo/Escabeche','Normal'))

#Pollo
lunchList.append(lunch('Pollo','Arroz con pollo/Ensalada rusa/Frijoles molidos.','Normal'))
lunchList.append(lunch('Pollo','Pollo deshuesado/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Pollo','Pollo empanizado/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(lunch('Pollo','Gordon blue/Arroz/Ensalda Verde/Aguacate/Verduras.','Premium'))
lunchList.append(lunch('Pollo','Lasaña con pollo/Ensalada Verde','Premium'))
lunchList.append(lunch('Pollo','Garbanzos con pollo','Normal'))
lunchList.append(lunch('Pollo','Arroz con palmito y pollo','Premium'))

#Spaghetti
lunchList.append(lunch('Spaghetti','Spaghetti con salsa roja y queso','Normal'))
lunchList.append(lunch('Spaghetti','ChopSuey','Normal'))
lunchList.append(lunch('Spaghetti','Spaghetti con pollo y salsa blanca/Brocoli','Normal'))
lunchList.append(lunch('Spaghetti','Spaghetti con pollo pesto','Premium'))
haySpaghetti = False

#Pescado
lunchList.append(lunch('Pescado','Pescado empanizado/Arroz/Frijoles/Patacones/Aguacate/Verduras.','Premium'))
lunchList.append(lunch('Pescado','Salmon/Arroz/Patacones/Aguacate/Verduras.','Premium'))
hayPescado = False

#Sopa
lunchList.append(lunch('Sopa','Sopa verdura.','Normal'))
lunchList.append(lunch('Sopa','Sopa de costilla/Elote/Yuca/Papa.','Normal'))
lunchList.append(lunch('Sopa','Sopa albondigas.','Normal'))
lunchList.append(lunch('Sopa','Sopa azteca.','Normal'))
haySopa = False


lunes= day(mealDay('','',lunch('','',''),lunch('','','')),'Lunes','Normal')
martes= day(mealDay('','',lunch('','',''),lunch('','','')),'Martes','Normal')
miercoles= day(mealDay('','',lunch('','',''),lunch('','','')),'Miercoles','Normal')
jueves= day(mealDay('','',lunch('','',''),lunch('','','')),'Jueves','Normal')
viernes= day(mealDay('','',lunch('','',''),lunch('','','')),'Viernes','Normal')
sabado= day(mealDay('','',lunch('','',''),lunch('','','')),'Sabado','Premium')

days=[lunes,martes,miercoles,jueves,viernes,sabado]
listaFinalBreakFast =[]
listaFinalSnacks =[]
listaFinalLuch =[]


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


# Reglas almuerzo
# 1. No repetir
# 2. viernes - sabado - domingo premium 
# 3. fijo 1 pescado 
# 4. sopa espaguetti no mas de uno

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

  if objeto_repetido(listaFinalLuch,valor.descp) == True:
    return False
  else:
    if premiumRules(valor,day) == False:
      return False
    else:
      if reglas_sopa_spaguetti(valor) == False:
        return False
      else:
        return True


def getLunch(day):
  valido = False
  while valido == False:
    valor = random.choice(lunchList)
    if validar_reglas(valor,day) == True:
      valido=True
    else:
      valido=False
  listaFinalLuch.append(valor.descp)















 



for day in days:
    randomBreakfast = getValorSinRepetir(breakfastList,listaFinalBreakFast)
    listaFinalBreakFast.append(randomBreakfast)
    randomSnack = getValorSinRepetir(snacksList,listaFinalSnacks)
    listaFinalSnacks.append(randomSnack)
    getLunch(day)
    print(day.dayName)
    print('-Desayuno:',randomBreakfast)
    print('-Merienda:',randomSnack)
    # print('-Almuerzo:',randomLunch.descp)
    print('--------')

print(listaFinalLuch)






