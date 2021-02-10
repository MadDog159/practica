costos = [20000,22000,2000,20400,20060,21100,2230,21000,230000,22000,23000,250000]
ventas = [50000,55000,51000,50020,50500,50070,50007,50800,57000,80000,70000,60000]

promedio_ganancia = 0
tabla_de_ganancia = []

for cost, sell in list(zip(costos, ventas)):
    resultado = sell - cost 
    resultado = (resultado/cost)*100
    tabla_de_ganancia.append(resultado)
average = sum(tabla_de_ganancia)/ len(tabla_de_ganancia)

print(f'promedio de ganancias {average}')

for x in range(12):
    resultado = ventas[x]-costos[x]
    resultado = (resultado/costos[x])*100
    #tabla_de_ganancia.append(resultado)
    promedio_ganancia = promedio_ganancia + resultado

promedio_ganancia = promedio_ganancia/12
print('el promedio de ganancia del year pasado es: {0:.2f} %'.format(promedio_ganancia))
print(f' {promedio_ganancia} %')
print(*tabla_de_ganancia, sep='\n')

