entry_number = int(input('Insira um número: '))
factorial = 1

for number in range(entry_number):
    factorial *= entry_number-number

if(entry_number < 0):
    print('Não é possível calcular o fatorial de um número negativo.')
else: print(factorial)