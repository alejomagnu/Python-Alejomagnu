# and ambas partes deben ser verdaderas para que como resultado de true

print ("AND")
print ("True and True =>", True and True) 
print ("True and False =>", True and False )
print ("False and True =>", False and False) 
print ("False and False =>", False and False) 


print (10 > 5 and 5  < 10 )

print (10 > 5 and 5  > 10 )

# Ejemplo practico sobre el stock o cantidad de productos que tiene una tienda o empresa en linea :

stock = input ("Ingrese el numero de stock =>")
stock  = int (stock)

# En este caso lo que se busca crear es que el sistema es que el stock no puede ser menor a 110 unidades pero tampoco mayor a 1000 unidades :

print (stock >= 110 and stock <= 1000)

# OR a diferencia de AND  Este operador informa que cualquiera de los dos lados que de True la operacion final seria True tambien

print ("OR")
print ("True or True =>", True or True) 
print ("True or False =>", True or False )
print ("False or True =>", False or True) 
print ("False or False =>", False or False) 


role = input ("Digita el rol =>")

print (role == "admin" or role == "seller")