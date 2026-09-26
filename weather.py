def average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)


def rainy_days(precipitation):
    return sum(1 for value in precipitation if value > 0)


def hottest_day(temperatures):
    return max(temperatures)
        
        
def coldest_day(temperatures):
    return min(temperatures)


def temperature_range(temperatures):
    return max(temperatures) - min(temperatures)