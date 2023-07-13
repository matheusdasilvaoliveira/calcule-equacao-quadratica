#Calcule a Equação Quadrática

import math

print ()

a = int(input('Insira o a: '))

b = int(input('Insira o b: '))

c = int(input('Insira o c: '))

delta = b ** 2 - 4 * a * c

x1 = round ((- b + math.sqrt (delta)) / (2 * a))

x2 = round ((- b - math.sqrt (delta)) / (2 * a))

print ()

print ("Delta = " + str (delta))

print ()

if delta > 0 :

    print ('Existem duas raízes reais e distintas, elas são ' + str (x1) + ' e ' + str (x2))

elif delta == 0 :
        
    print ('Exite apenas uma raíz que é ' + str (x1))
        
else :
        
    print('Não existem raízes reais')
