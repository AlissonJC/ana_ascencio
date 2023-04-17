price = float(input("Digite o preço do produto: R$ "))

discount = price * 0.10

new_price = price - discount

print(f"O novo preço é de: R$ {new_price:.2f}")