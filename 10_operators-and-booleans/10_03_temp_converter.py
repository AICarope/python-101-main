# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!
# C = F-32/1.8 formula
temperature = float(input("What is the Fahrenheit temperature today: "))
celsius = (temperature - 32) / 1.8
print(f"{temperature} in Fahrenheit is equal to {celsius} in Celsius")
