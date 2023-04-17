salary = float(input("Digite o valor salário: R$ "))
withdrawal_1 = float(input("Digite o valor do primeiro cheque: R$ "))
withdrawal_2 = float(input("Digite o valor do segundo cheque: R$ "))

cpmf_1 = withdrawal_1 * 0.38/100
cpmf_2 = withdrawal_2 * 0.38/100

balance = salary - withdrawal_1 - withdrawal_2 - cpmf_1 - cpmf_2
print(f"O saldo final é: R$ {balance:.2f}")