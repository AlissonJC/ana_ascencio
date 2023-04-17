number = float(input("Digite um número real: "))

integer_part = int(number)
fractional_part = number - integer_part
number_round = round(number)

print(f"Parte inteira: {integer_part}")
print(f"Parte fracionária: {fractional_part:.2f}")
print(f"Arredondamento: {number_round}")