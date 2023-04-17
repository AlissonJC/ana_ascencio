n1, n2, n3 = map(float, input("Digite as três notas: ").split())
p1, p2, p3 = map(float, input("Digite os pesos correspondentes: ").split())

total_pesos = p1 + p2 + p3
nota_1 = n1*p1
nota_2 = n2*p2
nota_3 = n3*p3

media = (nota_1 + nota_2 + nota_3)/total_pesos

print(f"A média é: {media:.1f}")