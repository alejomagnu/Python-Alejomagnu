name= " Manuel "
last_name = "Gutierrez  Mosquera"
print (name)
print (last_name)

full_name = name +""+ last_name 
print (full_name)

my_age = "25 años cumplidos el 27 de octubre"

quote = "I'am Manuel"
print (quote)
quote2 =  'she said "Hellow"'
print (quote2)

#format
template = " Hola, mi nombre es " + name + " y mi apellido es " + last_name

print (template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print (template)
template = f"hola, mi nombre es {name} y mi apellido {last_name}"
print (template)

template = f"Hola Mi nombre es {name} y Mi Apellido es {last_name} y Mi edad actual en el 2022 es {my_age}"
print (template)