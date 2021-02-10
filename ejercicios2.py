"""
holaaaa
"""

print("Convertidor de temperatura a Celsius")
temp = input("ingrese la temperatura de la sala: ")
temp = float(temp)

value = int(input("selecciona el tipo de temperatuta. Farenheit {1} o Kelvin {2}: " ))

if value < 1:
    value = 1
elif value > 2:
    value = 2
    
if value == 1:
    form1 = ((temp-32)* 5/9)
    temperatura_celsius = form1
else:
    form2 = (temp - 273.1)
    temperatura_celsius = form2
    
print(f'la temperatura celsius es {temperatura_celsius}')




