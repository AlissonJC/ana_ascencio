import math

step_height = float(input("Digite a altura de cada degrau: "))
target_height = float(input("Digite a altura que o usuário quer atingir: "))

steps_amount = int(math.ceil(target_height / step_height))

print(f"O usuário precisa subir {steps_amount} degraus.")