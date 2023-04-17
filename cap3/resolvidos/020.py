import math

degrees = float(input("Digite a medida do ângulo, em graus: "))
wall_height = float(input("Digite a altura da parede, em metros: "))

radian = degrees * 3.14 / 180
ladder = wall_height / math.sin(radian)

print(f"A altura da escada é de: {ladder:.2f}")