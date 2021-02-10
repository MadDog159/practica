num_vuelo = []
aerolineas = []
Aviones = []
multas = []

user = 'y'
while user == 'y':
    print("Bienvenidos al Instituto del Aeropuerto Internacional de Maiquetia")
    menu = input(' 1- ingresar vuelo de retraso.\n 2- Historial de retrasos.\n 3- Perdidas Totales')
    if menu == '1':

        Avion = input('Elija el Avion con el cual viajo: 767-300 ER (A) y 757-200 ER (B)')
        Avion.lower()
        if Avion == 'a':
            Avion = '767-300 ER'
            aerolinea = input('Elija la aerolinea con la cual viajo: Santa Barbara (S) y Aeropostal (A)')
            aerolinea.lower()
            if aerolinea == 's':

                multa = input('Indique en minutos el tiempo de retraso: ')
                numero = 0
                if multa.isnumeric():
                    multa = int(multa)
                    total = (multa*750)
                    numero = numero+1
                    print(total)
                    print(f'numero de vuelo es: {numero}')
                    
                    if Avion != '' and aerolinea != '' and total != '' and numero != '':
                        num_vuelo.append(numero)
                        aerolineas.append(aerolinea)
                        multas.append(total)
                        Aviones.append(Avion)
            elif aerolinea == 'a':
            

                multa = input('Indique en minutos el tiempo de retraso: ')
                numero = 0
                if multa.isnumeric():
                    multa = int(multa)
                    total = (multa*750)
                    numero = numero+1
                    print(total)
                    print(f'numero de vuelo es: {numero}')
                    
                    if Avion != '' and aerolinea != '' and total != '' and numero != '':
                        num_vuelo.append(numero)
                        aerolineas.append(aerolinea)
                        multas.append(total)
                        Aviones.append(Avion)
                        

                    
                    



                    
                
    
    
                else:
                    user = input('Informato incorrecto. Desea empezar (y/n): ')
        elif Avion == 'b':
            Avion = '757-200 ER'
            aerolinea = input('Elija la aerolinea con la cual viajo: Santa Barbara (S) y Aeropostal (A)')
            aerolinea.lower()
            if aerolinea == 's':
    
                multa = input('Indique en minutos el tiempo de retraso: ')
                numero = 0
                if multa.isnumeric():
                    multa = int(multa)
                    total = (multa*750)
                    numero = numero+1
                    print(total)
                    print(f'numero de vuelo es: {numero}')
                    
                    if Avion != '' and aerolinea != '' and total != '' and numero != '':
                        num_vuelo.append(numero)
                        aerolineas.append(aerolinea)
                        multas.append(total)
                        Aviones.append(Avion)
            elif aerolinea == 'a':
                multa = input('Indique en minutos el tiempo de retraso: ')
                numero = 0
                if multa.isnumeric():
                    multa = int(multa)
                    total = (multa*750)
                    numero = numero+1
                    print(total)
                    print(f'numero de vuelo es: {numero}')
                    
                    if Avion != '' and aerolinea != '' and total != '' and numero != '':
                        num_vuelo.append(numero)
                        aerolineas.append(aerolinea)
                        multas.append(total)
                        Aviones.append(Avion)
                        
            else:
                user = input('Avion inexistente. Desea empezar (y/n): ')
        else:
            user = input('Aerolinea inexistente. Desea empezar (y/n): ')
    else:
        user = input('No existe en el sistema: Desea empezar (y/n)')


