weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meter): "))
bmi = weight / (height ** 2)

print("Your BMI is {:.1f}".format(bmi))
