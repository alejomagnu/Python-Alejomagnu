# De un numero podemos transformarlo a un string  o de un string a un booleano y hacer una transformacion de tipos con codigo.

name = "Manuel"
print (type(name))
name = 12
print (type (name))
 # En la primera variable era un string luego se convirtio en un entero

name = True
print (type(name))

print (" Manu " + " " + " El crack ")
print (10 * 10)
print ("Manu" + "26")

age = 26

print ("Mi edad es" + str(age))
print (f"Mi edad es {age}")

# Se crea calculadora para saber tu edad en 10 años
age = input ("¿Cual es tu edad actual ?")
print (type(age))
age = int (age)
age += 10
print (f"Tu edad en 10 años sera {age}")

#