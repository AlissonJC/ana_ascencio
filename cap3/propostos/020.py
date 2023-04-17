import math

degrees = float(input("Digite a medida do ângulo: "))
distance = float(input("Digite a distância da escada para a parede: "))

radian = degrees * 3.1415 / 180

ladder_height = distance / math.sin(radian)

print(f"A altura da escada é de: {ladder_height:.2f}m")