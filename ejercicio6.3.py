tipos_de_movimiento = []
user_input = 'y'
while user_input == 'y':
    user_ID = input('ingrese cedula: ')
    user_pin = input('ingrese pin:')
    if user_pin == '1234':
    
        operaciones = input('que operacion va a realizar: consulta (c), deposito (d), retiro (r)')
        operaciones = operaciones.lower()
        if operaciones == 'd' or operaciones == 'r': 
    
            monto = input('monto: ')   
            if monto.isnumeric():
                tipos_de_movimiento.append((operaciones,monto))
            else:
                print('monto errado')
            
        elif operaciones == 'c':
            print(*tipos_de_movimiento,'\n')
        else:
            print('la operacion no existe')
           
    else:
        print('pin incorrecto')    
    user_input = input('desea continuar (y or n): ')  