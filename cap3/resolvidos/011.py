number = float(input("Digite um número positivo maior que zero: "))

square = number**2
cube = number**3
square_root = number**(1/2)
cubic_root = number**(1/3)

print(f"Quadrado de {number:.2f}: {square:.2f}")
print(f"Cubo de {number:.2f}: {cube:.2f}")
print(f"Raiz quadrada de {number:.2f}: {square_root:.2f}")
print(f"Raiz cúbica de {number:.2f}: {cubic_root:.2f}")