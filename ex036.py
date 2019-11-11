
casa = float(input('Digite o Valor da Casa: R$'))
sal = float(input('Digite o Seu salario: R$'))
anos = float(input('Digite em quantos anos você quer pagar: '))

prest = casa / (anos*12)
if prest > ((sal*30)/100):
    print('Emprestimo Negado')
else:
    print('Uma casa no valor de R$ {}, pagando em {} meses, sairá cada parcela no valor de R$ {}'.format(casa,anos,))

