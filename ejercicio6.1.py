

variable_x = range (1,11)
result = [(x**2 - x)**(1/2) for x in variable_x]

print(*list(zip(variable_x, result)), sep='\n')








