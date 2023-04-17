salary = float(input("Digite o salário: R$ "))

bonus = salary * 0.05
tax = salary * 0.07

income = salary - tax + bonus

print(f"Salário a receber: R$ {income:.2f}")