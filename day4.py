import calendar
# 1. Convert Kilometers to Miles
print("Convert Kilometers to Miles:")
kilometers_to_miles_conversion = 0.621371
distance_in_kilometers = float(input("Enter distance in kilometers: "))
distance_in_miles = distance_in_kilometers * kilometers_to_miles_conversion
print(f"{distance_in_kilometers} kilometers is equal to {distance_in_miles} miles.\n")

# 2. Convert Celsius to Fahrenheit
print("Convert Celsius to Fahrenheit:")
temperature_in_celsius = float(input("Enter temperature in Celsius: "))
temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
print(f"{temperature_in_celsius} degrees Celsius is equal to {temperature_in_fahrenheit} degrees Fahrenheit.\n")

# 3. Display Calendar
print("Display Calendar:")
year_to_display = int(input("Enter year: "))
month_to_display = int(input("Enter month: "))
print("\n" + calendar.month(year_to_display, month_to_display))

# 4. Swap Two Variables Without Temporary Variable
print("Swap Two Variables Without Temporary Variable:")
first_value = int(input("Enter the first value: "))
second_value = int(input("Enter the second value: "))
first_value, second_value = second_value, first_value
print(f"After swapping: first value = {first_value}, second value = {second_value}\n")
