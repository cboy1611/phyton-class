height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / ((height / 100) ** 2)
print("Your BMI is:", bmi)
if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You have a normal weight.")
elif bmi <= 29.9 :
    print("You are overweight.")
elif bmi <= 34.9:
    print ("you are severely overweight.")
elif bmi <= 39.9:
    print ("you are obese.")
else:
    print ("you are severely obese.")