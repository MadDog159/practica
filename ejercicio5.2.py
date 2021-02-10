num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

n = 26
count = 0
count_impar = 0
suma = 0

while count <= n and count_impar < 5:

    valor = num_list[count]
    if not valor % 2 == 0:
        count_impar = count_impar + 1
        suma = suma + valor

    
    count = count + 1
print(f'la suma de numeros impares es {suma}')

    


