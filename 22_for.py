                                                                                       #SE UTILIZA CUANDO YA TENEMOS UN NUMERO DE ELEMNTOS O ITERACIONES DADAS POR ALGUN ELEMENTO

'''
for element in range(1, 21):
  print (element)
'''  

my_list = [23,45,67,89,43]
for element in my_list:
  print (element)

my_tuple = ('manu', 'nico', 'kevin')
for element in my_tuple:
  print (element)


product = {
  'name': 'camisa',
  'price' : 100,
  'stock' : 89
}

for key in product:
  print (key,'=>', product[key])

for key, value in product.items():
  print(key, '=>', value )


people = [
  {'name' : 'manu',
   'age' : 25
   },
  {
    'name' : 'zule',
    'age': 45
    
  },
  {
    'name': 'santi',
    'age': 34
    
  }
]

for person in people:
  print ('name =>', person ['name'])

for person in people :
  print (person ['name'] ,'age =>', person ['age'])