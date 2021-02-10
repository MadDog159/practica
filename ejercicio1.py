name = input("Ingrese su nombre: ")
age = int(input("ingrese su edad: "))

current_year = 2020
year = (current_year - age) + 18

# concatenacion
# message = name + ' cumplio/cumplira 18 anos en '+str(year)

# format
message = "{}  cumpli/cumplira 18 anos en {}".format(name,year)

#message = f"{name} cumplio/cumplira 18 anos en {year}" 
print(message)
