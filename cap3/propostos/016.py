adjacent_leg = float(input("Digite o valor do cateto adjacente: "))
opposite_leg = float(input("Digite o valor do cateto oposto: "))

hypotenuse = (adjacent_leg ** 2 + opposite_leg ** 2) ** (1 / 2)

print(f"O valor da hipotenusa é de: {hypotenuse:.2f}")