lives = 3
print  (type(lives))
age= 12
budget = 100

temperature = 12.27
print (type(temperature))

lives = 2
print (lives)

lives = 1
print (lives)

lives = 12 + 15
print (lives)

lives = lives - 1
print (lives)

lives = lives - 1
print (lives)

lives -= 5
print (lives)

lives += 5
print (lives)


number = 1000000000000000000000000.1
print (number)

number = 15262000000000000000000000000.1
print (number)

# Reto de presupuesto :
#Formulamos pregunta y solicitamos datos de gasto en el mes de enero a marzo 2023

budget_enero =  float (input ("Cual es tu presupuesto de gasto en Enero"))
budget_febrero = float (input ("Cual es tu presupuesto de gasto en Febrero"))
budget_marzo =  float (input ("Cual es tu presupuesto de gasto en Marzo"))

#Almacenamos datos en una variable llamada  avg_mes dividimos en 3 para obtener el promedio

avg_mes = budget_enero + budget_febrero  + budget_marzo / 3

print ("El promedio de gasto mensual de enero a marzo de 2023 es de :", avg_mes)