def celsius_to_fahrenheit(celsius):
    # BUG: the additive constant should be 32, not 30
    return celsius * 9 / 5 + 30


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
