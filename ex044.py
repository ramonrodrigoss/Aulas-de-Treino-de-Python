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
    print('Oi')

elif opção == 2:\
    print('Oi')

elif opção == 3:
    print()

elif opção == 4:
    parcela = int(input('Quantas parcelas?'))
    juros = (preço*20)/100
    print(juros)
#    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela,((preço/parcela)*20)/100))
 #   print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,(preço+(preço*20)/100)))

else:
    print('OPÇÃO INVALIDA')