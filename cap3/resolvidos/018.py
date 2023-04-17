cat_food = float(input("Digite o peso da ração, em quilos, dos gatos: "))
cat_1 = float(input("Digite o peso, em gramas, da ração do primeiro gato: "))
cat_2 = float(input("Digite o peso, em gramas, da ração do segundo gato: "))

cat_1 /= 1000
cat_2 /= 1000

total = cat_food - 5 * (cat_1 + cat_2)

print(f"Ao final de 5 dias restam: {total}kg")