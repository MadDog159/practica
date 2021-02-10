user_input = 'y'
hora_de_reunion = 1
agenda = set()

while user_input == 'y':
    hora_de_reunion = input('Especifique su reunion en hora militar: ')
    if hora_de_reunion.isnumeric():
        hora_de_reunion = int(hora_de_reunion)
        if hora_de_reunion >=1 and hora_de_reunion <=24:
            agenda.add(hora_de_reunion)    
    
    user_input = input('desea continuar (y or n): ')
    user_input = user_input.lower()




print(*agenda, sep='\n')

