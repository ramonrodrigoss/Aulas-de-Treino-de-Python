#progressão aritmetica
termo = int(input('Digite o Valor do TERMO: '))
razão = int(input('Digite o Valor da RAZÃO: '))
décimo = termo +(10-1) * razão
for c in range(termo,décimo, razão):
    print(c,end=" -> ")
print('ACABOU!')