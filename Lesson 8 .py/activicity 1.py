# Program to check suitable clothes based on temperature

temp = int(input("Enter the temperature in °C:14  "))

if temp >= 25:
    print("You can wear light clothes.")
elif temp >= 15:
    print("The weather is moderate, wear something comfortable.")
else:
    print("Better wear warm clothes.")
