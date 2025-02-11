
weight = float(input("Enter your weight: "))

units = input("Your weight units Kilograms or Pounds\n Type Kg or Lbs: ").lower()

if units == 'kg':
    converted_weight = weight * 2.204
    unit = 'Lbs'
    print(f"Your actual weight {round(weight,2)}{units} and weight after conversion : {round(converted_weight, 2)}{unit}")

elif units == 'lbs':
    converted_weight = weight * 0.453
    unit = 'Kgs'
    print(f"Your actual weight {round(weight,2)}{units} and weight after conversion : {round(converted_weight, 2)}{unit}")

else:
    print(f"Invalid units{units}. Enter the units given in the options !")

