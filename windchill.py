# This first part is like the example that comes on the page

def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

# Input temperature and unit from the user
temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")

if unit.lower() == 'c':
    temperature_fahrenheit = (temperature * 9/5) + 32
    print(f"At temperature {temperature:.1f}C, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temperature_fahrenheit, 5):.2f}F")
    for wind_speed in range(10, 61, 5):
        print(f"At temperature {temperature:.1f}C, and wind speed {wind_speed} mph, the windchill is: {calculate_wind_chill(temperature_fahrenheit, wind_speed):.2f}F")
else:
    print(f"At temperature {temperature:.1f}F, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temperature, 5):.2f}F")
    for wind_speed in range(10, 61, 5):
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {calculate_wind_chill(temperature, wind_speed):.2f}F")



# And this other part is with a table type where the values are printed and everything
def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

def calculate_wind_chill(temperature, wind_speed):
    """Calculate wind chill based on temperature (in Fahrenheit) and wind speed (in mph)."""
    wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

def main():
    # Input temperature and unit from the user
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").lower()

    if unit == 'c':
        temperature = celsius_to_fahrenheit(temperature)

    # Display wind chill for wind speeds from 5 to 60 mph, in 5 mph increments
    print("\nWind Chill for Various Wind Speeds:")
    print(f"Temperature: {temperature:.1f}F")
    print("\nWind Speed (mph)\tWind Chill (°F)")
    print("-" * 35)

    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"{wind_speed}\t\t\t{wind_chill:.2f}F")

if __name__ == "__main__":
    main()