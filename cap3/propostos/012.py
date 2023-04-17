minimum_wage = float(input("Digite o valor do salário mínimo: R$ "))
employee_wage = float(input("Digite o valor do salário do funcionário: R$ "))

result = employee_wage / minimum_wage

print(f"O funcionário recebe {result:.2f} salários mínimos.")