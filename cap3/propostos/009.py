smaller_base = float(input("Digite o valor da base menor do trapézio: "))
higher_base = float(input("Digite o valor da base maior do trapézio: "))
height = float(input("Digite o valor da altura do trapézio: "))

area = ((smaller_base + higher_base) * height)/2

print(f"A área do trapézio é de: {area:.2f}ua")