if True: 
  print ("Deberia ejecutarse")

if False:
  print ("Nunca deberia ejecutarse")


pet = input ("¿Cual es tu mascota fav?")

if pet == "perro":

  print ("Genial tienes buen gusto")

elif pet == "gato" :
  print ("Muy buena suerte xD")

elif pet == "pez" :
  
  print ("Eres genial")
  
else : 
  
  print ("No tienes ninguna mascota fav, segun yo")

'''
stock = int (input ("Digita el stock =>"))

if stock >= 100 and stock <= 1000 :
  
  print ("El stock es correcto")
else :
  
  print ("El stock es incorrecto")           
             

'''          

# Reto crear una forma d eindentificar si un numero es par o impar

numero = int (input ("Digita un numero y te dire si es par o impar =>"))

if numero % 2 == 0 : 
  print ("Este numero es par")
  