#import json libreria para importar y usar los archivos json
status1=( "todo", "in-progress", "done") 
#lista de el progreso de las tareas se va dejar como una variable goblaL 
#para acceder a ella en cualquier momento
def task(t1): 
    #se define task para añadir las tareas  con un input que lo acomode como un diccionario
    #agregar la linea de codigo para jsn para que el diccionario se guarde 
    #hacer pruebas para verificar que se guarden como nuevos diccioanrio talvez como un for +=1 ?
  t1 = input(dict())
  #el diccionario solo tendra la key "id de la tarea" value "numero de la tarea "
  #key "nombre de la tarea" value "nombre o breve descripcion de la tarea"
  print(t1)
#se define estatus opciones con sentencias if para saber el estado de la tarea 
#se podria defininir en una sola funcion esta opcion  
def status(op):
  print("1.-todo \n2.-in-progress \n3-.done")
  op = int(input("mark the status of yours task"))
  if op ==1 :
    print
  elif op == 2:
    print()
  elif op ==3:
    print()
#pequeña funcion para elejir marcar o actualizar el estatus de la tarea  
  
