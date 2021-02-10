

def  fact_1(n):
    factorial_total = 1
    while n > 1:
        factorial_total = factorial_total * n
        n = n -1
    return factorial_total

n = int(input("escribe el valor de n:"))
k = int(input("escribe el valor de k:"))

operacion = fact_1(n)//(fact_1(k)*fact_1(n-k))

print(fact_1(n),fact_1(k), fact_1(n-k))
print(operacion)
    

#def combinatoria(n,k):
#    """[summary]
#
#    Args:
#        n (int): [description]
#        k (int): [description]
#    """
#
    