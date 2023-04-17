salary = float(input("Digite o salário fixo: R$ "))
sales = float(input("Digite o valor de vendas: R$ "))

commission = sales * 0.04

income = salary + commission

print(f"O valor da comissão é de: R$ {commission:.2f}")
print(f"O valor do novo salário é de: R$ {income:.2f}")