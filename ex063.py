print('-' * 25)
print('Sequencia de Fibonacci')
print('-' * 25)
mostrar = int(input('Quantos termos você quer mostrar? '))
contador = 1
novo = 1
anterior = 0
resultado = 0

print('~-~'*25)
print('{}'.format(anterior),end =' -> ')
print('{}'.format(novo),end=' -> ')

while contador <= (mostrar-2):
    resultado=anterior+novo
    print('{}'.format(resultado),end =" -> ")
    anterior = novo
    novo = resultado
    contador+=1
print('FIM')
print('~-~'*25)