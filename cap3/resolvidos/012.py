number_1, number_2 = map(float, input("Digite dois números positivos maiores que zero: ")
                         .split())

square_1 = number_1 ** number_2
square_2 = number_2 ** number_1

print(f"{number_1:.2f} elevado a {number_2:.2f} = {square_1:.2f}")
print(f"{number_2:.2f} elevado a {number_1:.2f} = {square_2:.2f}")