cost = float(input("Digite o preço do custo do espetáculo: R$ "))
ticket = float(input("Digite o preço do ingresso: R$ "))

amount = cost / ticket

print(f"A quantidade necessária para cobrir os custos é de {round(amount)} ingressos.")