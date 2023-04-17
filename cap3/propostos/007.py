weight = float(input("Digite o valor do peso: "))

gain_weight = weight * 1.15
lose_weight = weight - (weight * 0.20)

print(f"O novo peso após engordar 15% é de {gain_weight:.2f}")
print(f"O novo peso após emagrecer 20% é de {lose_weight:.2f}")