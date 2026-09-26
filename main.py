from weather import (
    average_temperature,
    rainy_days,
    hottest_day,
    coldest_day,
    temperature_range
)


temperatures = [12, 15, 20, 8, 17]
precipitation = [0, 5, 0, 10, 2]


print("Середня температура:", average_temperature(temperatures))
print("Днів з опадами:", rainy_days(precipitation))
print("Найвижа температура:", hottest_day(temperatures))
print("Найнижща температура:", coldest_day(temperatures))
print("Різниця температур", temperature_range(temperatures))