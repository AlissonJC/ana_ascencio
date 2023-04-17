worked_hours = int(input("Digite as horas trabalhadas: "))
minimum_wage = float(input("Digite o valor do salário mínimo: "))

value_hours = minimum_wage / 2
salary = worked_hours * value_hours
tax = salary * 0.03
income = salary - tax

print(f"Salário a receber: R$ {income:.2f}")