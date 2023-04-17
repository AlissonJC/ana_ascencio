import datetime

birth_year = int(input("Digite o ano de nascimento: "))

year_now = datetime.date.today().year

age = year_now - birth_year
year_2050 = 2050 - birth_year

print(f"A idade hoje é: {age}")
print(f"A idade em 2050 é: {year_2050}")