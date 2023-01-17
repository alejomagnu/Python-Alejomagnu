#CRUD : HACE REFERENCIA A CREAR,LEER, ACTUALIZAR Y BORRAR

#CREAR :
numbers = [1,2,3,4,5,6,7]
#LEER :
print (numbers [1])
#ACTUALIZAR :
numbers [-1] = 10

#CON APPEN SE AGREGAN ELEMENTOS EN DEFAULT AL FINAL DE LA LISTA
numbers.append (700)
print (numbers)

#TAMBIEN SE PUEDEN INSERTAR AL INICIO DE LA LISTA :

numbers.insert (0, 'hola')
print (numbers)

numbers.insert(3,'change')
print (numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']

#SE PUEDEN FUSIONAR LISTAS :
new_list = numbers + tasks
print (new_list)

#COMO SABER EN QUE POSICION ESTA UN ELEMENTOS ?

print (new_list.index ('todo2'))
new_list [index] = 'todo changed'

print (new_list)

#COMO REMOVER ELEMENTOS :

new_list.remove ('todo 1')
print (new_list)

#CON POP SE PUEDE REMOVER TAMBIEN :

new_list.pop()
print (new_list) 

new_list.pop (0)
print (new_list)

new_list.reverse()
print (new_list)

#ORDENDA DEL MENOR A EL MAYOR CON SORT

numbers_a = [1,4,6,3,7,2,50,25,100,12]
numbers_a.sort()

print (numbers_a)

strings = ['re','ab','ed']
strings.sort()
print (strings)