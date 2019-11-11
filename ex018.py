from math import cos,sin,tan, radians

ang = float(input('Digite o ângulo para calcularmos o SENO, COSSENO e TANGENTE \n'))

print('O SENO desse ângulo é {:.2f}\nO COSSENO é {:.2f}\nE a TANGENTE é {:.2f}'.format(sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))