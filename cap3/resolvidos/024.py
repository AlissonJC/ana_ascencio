hour_complete = float(input("Digite a hora como um número real: "))

hour = int(hour_complete)
minute = hour_complete - hour

conversion = (hour * 60) + (minute * 100)

print(f"Os minutos da hora são: {conversion}")