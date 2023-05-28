import Clases
# BASE DE DATOS
breakfastList=['Pinto con huevo','Pinto con queso','Huevos con tortilla','Prensadas queso y frijol','Tortilla con queso','Sandwich con jamon','Sandwich con huevo','Tostadas con aguacate y huevo','Omelette']
snacksList=['Batido de banano','Batido de melón','Batido de papaya','Uvas','Manzana picada','Mango picado','Yogurt y granola con una fruta']
lunchList=[]

# CARNE ROJA
lunchList.append(Clases.lunch('Carne','Tortas carne/Arroz/Frijoles/Ensalda Verde/Agucate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Bistek encebollado/Arroz/Frijoles/Ensalda Verde/Agucate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Fajitas de carne/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Lentejas con carne desmechada/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Canelones con carne desmechada/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Carne en salsa/Arroz/Frijoles/Caracoles/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Arroz chino/Ensalada Verde','Normal'))
lunchList.append(Clases.lunch('Carne','Picadillo arracache con carne/arroz','Normal'))

# CARNE BLANCA
lunchList.append(Clases.lunch('Carne','Chifrijo','Premium'))
lunchList.append(Clases.lunch('Carne','Garbanzos con cerdo/Escabeche','Normal'))
lunchList.append(Clases.lunch('Carne','Chuleta cerdo/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Chuleta ahumada/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Costilla cerdo frita/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Carne','Frijoles blancos con cerdo/Escabeche','Normal'))
lunchList.append(Clases.lunch('Carne','Frijoles tiernos con cerdo/Escabeche','Normal'))

# POLLO
lunchList.append(Clases.lunch('Pollo','Arroz con pollo/Ensalada rusa/Frijoles molidos.','Normal'))
lunchList.append(Clases.lunch('Pollo','Pollo deshuesado/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Pollo','Pollo empanizado/Arroz/Frijoles/Ensalda Verde/Aguacate/Verduras.','Normal'))
lunchList.append(Clases.lunch('Pollo','Gordon blue/Arroz/Ensalda Verde/Aguacate/Verduras.','Premium'))
lunchList.append(Clases.lunch('Pollo','Lasaña con pollo/Ensalada Verde','Premium'))
lunchList.append(Clases.lunch('Pollo','Garbanzos con pollo','Normal'))
lunchList.append(Clases.lunch('Pollo','Arroz con palmito y pollo','Premium'))

# SPAGUETTI
lunchList.append(Clases.lunch('Spaghetti','Spaghetti con salsa roja y queso','Normal'))
lunchList.append(Clases.lunch('Spaghetti','ChopSuey','Normal'))
lunchList.append(Clases.lunch('Spaghetti','Spaghetti con pollo y salsa blanca/Brocoli','Normal'))
lunchList.append(Clases.lunch('Spaghetti','Spaghetti con pollo pesto','Premium'))

# PESCADO
lunchList.append(Clases.lunch('Pescado','Pescado empanizado/Arroz/Frijoles/Patacones/Aguacate/Verduras.','Premium'))
lunchList.append(Clases.lunch('Pescado','Salmon/Arroz/Patacones/Aguacate/Verduras.','Premium'))

# SOPAS 
lunchList.append(Clases.lunch('Sopa','Sopa verdura.','Normal'))
lunchList.append(Clases.lunch('Sopa','Sopa de costilla/Elote/Yuca/Papa.','Normal'))
lunchList.append(Clases.lunch('Sopa','Sopa albondigas.','Normal'))
lunchList.append(Clases.lunch('Sopa','Sopa azteca.','Normal'))

listaFinalBreakFast =[]
listaFinalSnacks =[]
listaFinalLuchNames =[]
listaFinalLuchObjs =[]
lunes= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Lunes','Normal')
martes= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Martes','Normal')
miercoles= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Miercoles','Normal')
jueves= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Jueves','Normal')
viernes= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Viernes','Normal')
sabado= Clases.day(Clases.mealDay('','',Clases.lunch('','',''),Clases.lunch('','','')),'Sabado','Premium')
days=[lunes,martes,miercoles,jueves,viernes,sabado]




