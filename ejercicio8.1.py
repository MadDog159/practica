#secciones = [
#    ['Maria', 'Andres', 'Pedro'],
#    ['Stefania', 'Gabriel', 'julia', 'Manuel']
#    ]
#
#for seccion in secciones:
#   for estudiante in seccion:
#       print("El nombre del estudiante es: {}".format(estudiante))

#secciones = [
#    ['Maria', 'Andres', 'Pedro'],
#    ['Stefania','gabriel', 'julia', 'Manuel']
#]
#
#for i in range(len(secciones)):
#   for j in range(len(secciones[i])):
#       print("El nombre del estudiante es: {}".format(secciones[i][j]))

#elementos = [{
#    "nombre": "hidrogeno",
#    "numero": 1,
#    "peso": 1.00794,
#    "simbolo": "H"
#},
#{
#    "nombre": "helio",
#    "numero": 2,
#    "peso": 4.002602,
#    "simbolo": "He"
#}
#]
#
#for elemento in elementos:
#  print('nombre: {} - Simbolo: {}'.format(elemento["nombre"], elemento["simbolo"]))


matrix = [
    [1,4,5],
    [4,2,6],
    [5,6,3]
]

result = True

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix [j][i]:
            result = False
if result:
    print("simetrica")
else:
    print("no simetrica")       