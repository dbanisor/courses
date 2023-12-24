height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi_index_not_rounded = weight/ height ** 2
bmi_two_digits = round(bmi_index_not_rounded, 2)
bmi_index = round(weight/height ** 2)

if bmi_two_digits <= 18.5:
    print(f"Your BMI is {bmi_index}, you are underweight.")
elif bmi_two_digits > 18.5 and bmi_two_digits <= 25:
    print(f"Your BMI is {bmi_index}, you are normal weight.")
elif bmi_two_digits > 25 and bmi_two_digits <= 30:
    print(f"Your BMI is {bmi_index}, you are slightly overweight.")
elif bmi_two_digits > 30 and bmi_two_digits <= 35:
    print(f"Your BMI is {bmi_index}, you are obese.")
else:
    print(f"Your BMI is {bmi_index}, you are clinically obese.")