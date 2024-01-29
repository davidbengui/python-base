#Tabuada dos numeros de 1 a 10

numeros = list(range(1,11))
for numero in numeros:
    print("Tabuada do numero",numero)
    for novo_numero in numeros:
        print(numero * novo_numero)
    print("--------------")