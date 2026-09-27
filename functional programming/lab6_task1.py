def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
temperatures = [0, 10, 20, 30, 40]
fahrenheit = list(map(celsius_to_fahrenheit, temperatures))
print("Celsius:", temperatures)
print("Fahrenheit:", fahrenheit)
output:
Celsius: [0, 10, 20, 30, 40]
Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]

