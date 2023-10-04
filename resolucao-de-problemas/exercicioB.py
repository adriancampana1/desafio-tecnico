def calculate_sum_of_even_and_product_of_odd(numbers):
    sum_of_even = 0
    product_of_odd = 1

    for number in numbers:
        if number % 2 == 0:
            sum_of_even += number
        else:
            product_of_odd *= number

    return sum_of_even, product_of_odd

entry_value = input('Insira uma lista de números separados por vírgula (1,2,3,4): ').split(',')
input_list = [int(x) for x in entry_value]

sum_of_even, product_of_odd = calculate_sum_of_even_and_product_of_odd(input_list)

print(f"Soma dos pares: {sum_of_even}")
print(f"Produto dos ímpares: {product_of_odd}")