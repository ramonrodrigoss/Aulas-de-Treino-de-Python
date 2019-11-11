n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um outro numero: '))
n3 = int(input('Digite mais um numero:'))

if n1 == n2 and n1 == n3:
    print('Voce digitou numeros iguais!')
exit()

#verifica quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verifica o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior é {} !'.format(maior))
print('O menor é {} !'.format(menor))