vel = float(input('Digite a Velocidade de seu carro: \n'))
if vel > 80:
    print('Voce passou do limite! e tera que pagar uma multa no valor de R${:.2f} !'.format((vel-80)*7.00))
else:
    print('Voce esta dentro do limite! Parabens')