salary = float(input("Digite o valor do salário: R$ "))
bill_1 = float(input("Digite o valor da primeira conta: R$ "))
bill_2 = float(input("Digite o valor da segunda conta: R$ "))

bill_1 = bill_1 * 1.02
bill_2 = bill_2 * 1.02

balance = salary - bill_1 - bill_2

print(f"O restante do salário é de: R$ {balance:.2f}")