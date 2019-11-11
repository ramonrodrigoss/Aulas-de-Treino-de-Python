import datetime
x = datetime.datetime.now()

print('Verificador de Alistamento Militar')
ano = int(input('Digite o ANO que você nasceu: '))

alistamento = x.year - ano
if alistamento >= 18 and alistamento < 25:
   print('Você ainda pode se alistar')
elif alistamento < 18:
   print('Voce é muito novo para se alistar')
else:
   print('Você já passou da hora de se alistar!!!')



