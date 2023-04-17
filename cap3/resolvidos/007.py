salary = float(input("Digite o salário: R$ "))

bonus = 50
tax = salary * 0.1

income = salary + bonus - tax

print(f"Salário a receber: R$ {income:.2f}")