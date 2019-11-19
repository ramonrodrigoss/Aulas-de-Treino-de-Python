from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range(1,8,1):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if data-ano < 18:
        menor += 1
    elif data-ano >= 18:
        maior +=1
print('''Ao todo, tivemos {} pessoas maiores de idade
E Também tivemos {} pessoas menores de idade'''.format(maior,menor))
