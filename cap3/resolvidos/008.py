deposit = float(input("Digite o valor do depósito: R$ "))
interest = float(input("Digite o percentual da taxa de juros: "))

profit = deposit * interest/100

total = deposit + profit

print(f"O rendimento líquido é de: R$ {profit:.2f}")
print(f"O total de retorno é de: R$ {total:.2f}")