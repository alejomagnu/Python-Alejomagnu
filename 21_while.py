#CICLOS "MIENTRAS"
'''
while True:
  print ('se ejecuto')

'''
# CONTADOR QUE SUME UNO MIENTRAS EL NUMERO SEA MENOR A 10 CUANDO LLEGUE A 10 SE DETIENE ESE ES UN CICLO
counter = 0
'''
while counter < 10 :
  counter += 1
  print (counter)

#BREAK SIRVE PARA DETENER EL CICLO
counter= 0
while counter <20:
  counter += 1
  if counter == 15:
    break
  print (counter)
'''

counter = 0

while counter < 20:
  counter += 1
  if counter < 15:
    continue
print (counter)  