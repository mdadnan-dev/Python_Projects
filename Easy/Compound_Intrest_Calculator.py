
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter a principle amount: "))
    if principle <= 0:
        print("Value cannot be less than or equal to zero.")
    else:
        break

while True:
    rate = float(input("Enter rate of intrest: "))
    if rate < 0:
        print("Value cannot be less than zero.")
    else:
        break

while True:
    time = int(input("Enter a time period: "))
    if time <= 0:
        print("Value cannot be less than or equal to zero.")
    else:
        break


total = ( principle * ( pow(1 + (rate / 100), time) ) )

print(f"Your principle amount is {principle}\nYour Rate of Intrest is {rate}\nTime Period is {time}\nYour Total is {round(total, 2)}")