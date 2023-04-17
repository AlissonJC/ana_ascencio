ladder_height = float(input("Digite o tamanho da escada, em metros: "))
wall_height = float(input("Digite o tamanho da parede, em metros: "))

distance_to_wall = (ladder_height**2 - wall_height**2)**(1/2)

print(f"A distância para a parede deve ser de: {distance_to_wall:.2f}m")