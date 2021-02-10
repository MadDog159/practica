def numeros(*n):
    media = sum(n)/len(n)
    result = 0
    for x in n:
        result = result + (x - media)**2
    result = result/len(n)
    return media, result

n = [x for x in range(100)]
print(numeros(*n))



