wide = float(input("Digite a largura do cômodo: "))
length = float(input("Digite o comprimento do cômodo: "))

dimension = wide * length
power = dimension * 18

print(f"A área do cômodo é: {dimension:.2f} metros quadrados.")
print(f"A potência necessária é de: {power:.2f} Watts de potência.")