price = float(input("Digite o preço de fábrica: R$ "))
profit = float(input("Digite o percentual de lucro do distribuidor: "))
taxes = float(input("Digite o percentual de imposto: "))

profit_value = price * profit/100
taxes_value = price * taxes/100
final_price = price + profit_value + taxes_value

print(f"O lucro do distribuidor é: R$ {profit_value:.2f}")
print(f"O valor dos impostos é de: R$ {taxes_value:.2f}")
print(f"O valor final do carro é de: R$ {final_price:.2f}")