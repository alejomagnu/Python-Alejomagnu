person = {

'name' : 'alejo',
 'last_name' : 'gutierrez', 
  'langs' : [ 'python','javascript' ],
  'age' : 99
}

print (person)

#PARA ACTULIZAR DATOS SE HACE ASI :

print (person)

person ['name'] = 'Manuel'
person ['age'] -= 50
person ['langs'].append ('rust')
print (person)

#ELIMINAR UN DATO

del person ['last_name']
person.pop('age')
print (person)

print ('items')
print (person.items ())

print ('keys')
print (person.keys ())

print ('values')
print (person.values ())
