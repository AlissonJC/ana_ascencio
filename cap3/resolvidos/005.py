salary = float(input("Digite o salário: R$ "))
salary_raise = float(input("Digite o percentual de aumento: "))

increase = salary * salary_raise/100
new_salary = salary + increase
print(f"Novo salário: R$ {new_salary:.2f}")