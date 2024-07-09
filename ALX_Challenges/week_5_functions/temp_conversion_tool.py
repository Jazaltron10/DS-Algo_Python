# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == "C":
        convert_to_fahrenheit(temperature)
    elif unit == "F":
        convert_to_celsius(temperature)
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
if __name__ == "__main__":
    main()



# FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# def convert_to_celsius(fahrenheit):
#     print("amen")
    


# def convert_to_fahrenheit(celsius):
#     print("amen")
    


# def main():
#     temperature = float(input("Enter the teperature to convert: "))
#     unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
#     if unit == "C":
#         convert_to_fahrenheit(temperature)
#     elif unit == "F":
#         convert_to_celsius(temperature)
#     else:
#         print(f"Invalid temperature. Please enter a numeric value.")
        
        
# if __name__ == "__main__":
#     main()
