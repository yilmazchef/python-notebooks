# calculate the BMI of a person
# BMI = weight / height^2

# read the weight and height from the user

weight = input("Enter your weight in kg: ")
# converteer de ingevoerde waarde naar een juist type
weight = float(weight)

height = input("Enter your height in meters: ")
# converteer de ingevoerde waarde naar een juist type
height = float(height)

bmi = weight / height ** 2
bmi = round(bmi, 2)

# 1.567 -> round(1.567, 2) -> 1.57
# 1.543 -> round(1.543, 2) -> 1.54
# 1.5555555555555555555555555555555555555558 


# bereken het BMI (Body Mass Index)

# Wikipedia: https://en.wikipedia.org/wiki/Body_mass_index
# BMI < 18.5: Underweight
# 18.5 <= BMI < 25: Normal
# 25 <= BMI < 30: Overweight
# BMI >= 30: Obese

# print the BMI and the category

is_underweight = bmi < 18.50
is_normal = 18.50 <= bmi < 25.00
is_overweight = 25.00 <= bmi < 30.00
is_obese = bmi >= 30.00

print("Your BMI is: " + str(bmi))
print("You are underweight: " + str(is_underweight))
print("You are normal: " + str(is_normal))
print("You are overweight: " + str(is_overweight))
print("You are obese: " + str(is_obese))


