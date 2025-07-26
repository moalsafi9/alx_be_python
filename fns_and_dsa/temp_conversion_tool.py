FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

def ui():
    temp = int(input("Enter the temperature to convert: "))
    deg = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if deg.upper() == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C") 
    elif deg.upper() == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F") 
    else:
        print("Invalid input. Please enter C or F.")

ui()
