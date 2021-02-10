name = input("Nombre: ")
last_name = input("Apellido: ")
age = int(input(("edad: ")))
print(f'tu nombre tiene {len(name)} letras')
print(f'tu apellido tiene {len(last_name)} letras')

print(f'tu posiblemente naciste en el {2020 - age} {2020 - (age+1)}')

if len(name) >= 6:
    print("dude tu nombre tiene muchos caracteres")
