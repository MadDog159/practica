#OUTPUT
#Hay {} frutas en la cesta. y {} objetos que no son frutas.

# Variable Globales
Cantidad_frutas, cantidad_no_frutas = 0, 0

cesta = {'manzanas': 4, 'naranjas': 19, 'hamburguesa': 3, 'sandwiches': 8}

frutas = ['manzanas', 'naranjas', 'peras', 'parchitas', 'uvas', 'cambures']


for alimento, cantidad in cesta.items():
    if alimento in frutas:
        Cantidad_frutas += cantidad
    else:
        cantidad_no_frutas += cantidad

print(f'Hay {Cantidad_frutas} frutas en la cesta. y {cantidad_no_frutas} objetos que no son frutas')