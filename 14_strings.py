text = 'Ella sabe programar en Python'
'''
print ('JavaScript' in text)
print ('Python' in text)

if 'Python' in text :
  print ('Elegiste bien')
else :
  print ('Tambien elegiste bien')
'''


# size cuenta los espacios y caracteresm, tambien puede transformar los strings o cadenas de texto a mayusculas o minuscula etc..

size = len (text)
print (size)
print (text)
print (text. upper())
print (text. lower ())
print (text. count ('a'))


#SWAPCASE SIRVE PARA CAMBIAR O TRANSFORMAR O INVERTIR EL ESTADO ACTUAL DE UNA LETRA O STRING  A SU ESTADO CONTRARIO, ES DECIR DE MAYUSCULA TRANSFORMA A MINUSCULA Y DE MINUSCULA TRANSFORMA A MAYUSCULA

print (text.swapcase ())

print (text . startswith ('Ella'))
print (text. endswith ('Rust'))
print (text. replace ('Python' , 'Go'))

text_2 = 'este es un titutlo'
print (text_2)
print (text_2 . capitalize ())
print (text_2. title ())
print (text_2. isdigit ())
print ("389654". isdigit ())