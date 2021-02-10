
list_year_bisi = []
list_year_capi = []
for years in range(1921,2022,1):

    if years % 4 == 0:
        list_year_bisi.append(years)


    if str(years) == str(years)[::-1]:
        list_year_capi.append(years)


print(f'lista de year capicua de los ultimos 100 year{list_year_capi}')
print(f'lista de year bisiesto de los ultimos 100 year {list_year_bisi}')








