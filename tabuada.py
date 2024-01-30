"""
__version__ = "0.1.1"
__authot=__"david"

template = 
"""



numeros = list(range(1,11))
for n1 in numeros:
    print("{:-^20}".format(f"Tabuada de Multiplicar do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:-^18}".format(f"{n1} x {n2} = {resultado}"))
         
    print("#" * 18)

for n1 in numeros:
    print("{:-^20}".format(f"Soma do Nº {n1}".center(60)))
    print()
    for n2 in numeros:
        soma = n1 + n2
        print("{:-^18}".format(f"{n1} + {n2} ={soma}".center(60)))
    print ("#" *70 )
