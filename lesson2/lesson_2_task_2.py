def is_year_leap(year):
    return year % 4 == 0


year_to_check = 2020
is_leap_year = is_year_leap(year_to_check)
print(f"Год {year_to_check} является високосным: {is_leap_year}")