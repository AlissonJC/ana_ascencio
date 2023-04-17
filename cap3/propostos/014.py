import datetime

birth_year = int(input("Digite o ano de nascimento: "))
year_now = datetime.date.today().year

age_years = year_now - birth_year
age_months = age_years * 12
age_days = age_months * 30
age_weeks = age_months * 4

print(f"A idade em anos é de: {age_years}")
print(f"A idade em meses é de: {age_months}")
print(f"A idade em dias é de: {age_days}")
print(f"A idade em semanas é de: {age_weeks}")