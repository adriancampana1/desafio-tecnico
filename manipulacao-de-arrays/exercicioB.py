entry_number = input('Insira uma lista de números separados por vírgula (1,2,3,4): ').split(",")

formatted_list = []

for item in entry_number:
    if int(item) not in formatted_list:
        formatted_list.append(int(item))
 
print(formatted_list)