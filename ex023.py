num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))







#print('Programa que vai mostrar cada digito separado')
#num = str((input('Digite um numero entre 0 e 9999 :\n')))
#print('A unidade é ', num[3])
#print('A dezena é', num[2])
#print('A centena é,',num[1])
#print('A Milhar é',num[0])
#