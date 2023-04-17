worked_hours = int(input("Digite o número de horas trabalhadas: "))
minimum_wage = float(input("Digite o valor do salário mínimo: R$ "))
extra_hours = int(input("Digite o número de horas extras: "))

worked_hour_value = minimum_wage / 8
extra_hour_value = minimum_wage / 4
salary = worked_hour_value * worked_hours + extra_hour_value * extra_hours

print(f"O salário a receber é de: R$ {salary:.2f}")