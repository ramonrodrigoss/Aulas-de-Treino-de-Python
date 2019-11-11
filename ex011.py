print('Programa de calculo da Área de um quarto e tambem mostre quantos litros de tinta serão necessários para pinta-lo ')
lar=float(input('Digite a Largura da parede\n'))
alt=float(input('Digite a Altura da parede\n'))
area=alt*lar
print('A área é de {}m², e você gastará {}lt para pintar todo o quarto!'.format(area,area/2))