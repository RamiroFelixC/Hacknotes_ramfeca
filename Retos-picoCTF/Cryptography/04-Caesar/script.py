import string 
import re

abc=string.ascii_letters

encryp = open('ciphertext','r').read()
encryp = re.findall('\{(.*?)\}', encryp)[0]

rot = 25
salida = ''
for car in encryp:
    salida+= abc[(abc.find(car)+rot)%26]

print(salida)
    
