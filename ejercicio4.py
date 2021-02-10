monto = input("monto de la compra: ")


if monto.isnumeric():
    monto = float(monto)

    if 0 <= monto <= 800:
        print(f'pago total {monto}')
    elif 800 < monto <= 1500:
        print(f'aplica 10%, total = {monto*0.9}')
    elif 1500 < monto <= 5000:
        print(f'aplica 15%, total = {monto*0.85}')
    else:
        print(f'aplica 20%, total = {monto*0.8}')
else:
    print("por favor ingresar un valor numerico")

