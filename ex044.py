print('Gerenciador de Pagamentos')
preço = float(input('Preço das compras: R$'))
opção = int(input ("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão

Qual é a opção?
"""))
if opção == 1:
    print('O Valor da compra é de R${:.2f} e com o desconto de 10% fica R${:.2f}'.format(preço,preço-(preço*10/100)))

elif opção == 2:\
    print('O Valor da compra é de R${} e com o desconto de 5% fica R${}'.format(preço,preço-(preço*5/100)))

elif opção == 3:
    print('O Valor da compra é de R${}, nesssa forma de pagamento não tem desconto'.format(preço))
    print('As parcelas ficam no valor de R${}'.format(preço/2))

elif opção == 4:
    parcela = int(input('Quantas parcelas?'))
    juros = (preço+(preço*20)/100)/parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela,juros))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,(preço+(preço*20)/100)))

else:
    print('OPÇÃO INVALIDA')