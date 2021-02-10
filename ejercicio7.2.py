# podemos crear un diccionario, contador, que realiza un seguimiento del recuento total de cada palabra en la lista quote.

#output esperado:
#{'tienes': 1, 'que': 1, 'bailar': 1, 'como':4, 'si': 4, 'no': 2, 'hubiera': 2, 'nadie': 2, 'mirando': 1, 'ama': 1, 'nunca': 1, 'te': 1, 'lastimaran': 1, 'canta': 1, 'escuchando': 1, 'y': 1, 'vive': 1, 'fuera': 1, 'el': 1, 'cielo': 1, 'en': 1, 'la': 1, 'tierra': 1}


contador = {}
quote = ['tienes', 'que', 'bailar', 'como', 'si', 'no', 'hubiera', 'nadie', 'mirando', 'ama', 'como', 'si', 'nunca', 'te', 'lastimaran', 'canta', 'como', 'si', 'no', 'hubiera', 'nadie', 'escuchando', 'y', 'vive', 'como', 'si', 'fuera', 'el', 'cielo', 'en', 'la', 'tierra']

#list_quote = set(quote)
#list_quote = list(list_quote)
#for spalabra in list_quote:
#    valor = quote.count(spalabra)
#    contador.setdefault(spalabra,valor)
#
#print(contador)
print(contador)
for palabra in quote:
    contador[palabra] = contador.get(palabra, 0)+ 1
print(contador)
    

