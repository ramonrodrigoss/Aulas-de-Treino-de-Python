print('Programa para calcular a Porcentagem de um preço!')
p=float(input('Digite o valor do produto:\n'))
print('O Produto custa R${:.2f} e com o desconto de 5% ele vai sair por R${:.2f}'.format(p,(p/100)*95))