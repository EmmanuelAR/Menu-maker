import Clases
import DB
import Utils
import pywhatkit
from datetime import date



#Grupo fam
# pywhatkit.sendwhatmsg_to_group_instantly( "IaYp8vSmcDBHxCV6vLZ8MO","Hola prueba")
 

#Grupo mio
# pywhatkit.sendwhatmsg_to_group_instantly( "D5OZ4sbFVYeDq4xrgpqwxe","Hola prueba")

if __name__ == '__main__':

  respuesta = ''

  while respuesta != 'SI' and respuesta != 'Si' and respuesta != 'si' :
    Utils.resetVariables()
    fecha_actual = date.today()
    message='------ Menu Semana: '+str(fecha_actual)+' ------'+'\n\n'
    for day in DB.days:
        randomBreakfast = Utils.getValorSinRepetir(DB.breakfastList,DB.listaFinalBreakFast)
        DB.listaFinalBreakFast.append(randomBreakfast)
        randomSnack = Utils.getValorSinRepetir(DB.snacksList,DB.listaFinalSnacks)
        DB.listaFinalSnacks.append(randomSnack)
        randomLunch = Utils.getlunch(day)
        day.mealDay = Clases.mealDay(randomBreakfast,randomSnack,randomLunch,randomLunch)
        message +='        '+day.dayName+'\n'
        message +='-Desayuno  -> '+ day.mealDay.breakFast+'\n'
        message +='-Merienda  -> '+ day.mealDay.snack+'\n'
        message +='-Almuerzo  -> '+ day.mealDay.lunch.descp+'\n\n'
    message+='TE QUEREMOS MUCHO MA, GRACIAS POR COCINAR <3\n'
    print(message)
    respuesta = input("Le parece el menu? (si - no) ")
  pywhatkit.sendwhatmsg_to_group_instantly( "IaYp8vSmcDBHxCV6vLZ8MO",message)





