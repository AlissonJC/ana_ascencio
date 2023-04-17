minimum_wage = float(input("Digite o valor do salário mínimo: R$ "))
kilowatt_amount = float(input("Digite a quantidade de kilowatts consumida: "))

kilowatt_value = minimum_wage / 5
electricity_bill = kilowatt_value * kilowatt_amount

discount = electricity_bill * 0.15

final_bill = electricity_bill - discount

print(f"O valor do kilowatt é de: R$ {kilowatt_value:.2f}")
print(f"O valor bruto a ser pago é: R$ {electricity_bill:.2f}")
print(f"O valor a ser pago com disconto é de: R$ {final_bill:.2f}")