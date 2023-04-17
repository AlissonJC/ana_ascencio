hour = int(input("Digite o valor da hora: "))
minute = int(input("Digite o valor dos minutos: "))

hour_to_minute = hour * 60
minutes = minute + hour_to_minute
seconds = minutes * 60

print(f"Hora digitada convertida em minutos: {hour_to_minute}")
print(f"Total dos minutos: {minutes}")
print(f"Total dos segundos: {seconds}")