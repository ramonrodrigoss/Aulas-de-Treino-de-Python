print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
quant = maiormil = soma = menorp = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    if preço > 1000:
        maiormil += 1
    if quant == 0 or preço < menorp:
        menorp = preço
        barato = produto
    soma +=preço
    continuar = str(input('Quer Continuar? [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar =input('opção Invalida [S / N]')
    if continuar in 'n':
        break
print(f'''O total da compra foi R${soma:.2f}
Temos {maiormil} produtos custando mais de R$1000.00
O Produto mais barato foi {barato} que custa R${menorp:.2f} 
''')