v = float(input('Digite a quantidade de KM rodados na sua viagem: '))
if v <= 200:
    print('Você vai pagar {} pela sua viagem'.format(v * 0.50))
else:
    print('Você vai pagar {} pela sua viagem'.format(v * 0.45))
