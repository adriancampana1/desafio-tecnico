entry_number = input('Insira uma lista de números separados por vírgula (1,2,3): ').split(',')

max_number = 0
for index in entry_number:
    if int(index) > max_number:
        max_number = int(index)
print(max_number)