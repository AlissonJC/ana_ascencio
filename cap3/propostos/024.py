amount = float(input("Digite a quantidade de dinheiro em reais: R$ "))

dollar = amount / 1.80
german_mark = amount / 2.00
british_pound = amount / 3.57

print(f"US Dollar: {dollar:.2f}")
print(f"German Mark: {german_mark:.2f}")
print(f"British Pound: {british_pound:.2f}")