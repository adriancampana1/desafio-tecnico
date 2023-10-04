entry_number = int(input('Insira um ano: '))

if entry_number % 4 == 0 and entry_number % 100 != 0 or entry_number % 400 == 0:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')