# Body Mass Index (BMI) is a measure of body fat based on an individual's weight and height. 
# It is commonly used as a screening tool to categorize individuals into different weight status categories, such as underweight, normal weight, overweight, and obesity.
# The BMI is calculated using the following formula:
# BMI = Weight (kg) / Height (m)^2

# Alternatively, in the imperial system:
# BMI = (Weight (lb) /Height (in)^2) × 703

# BMI provides a general indication of body fatness but does not directly measure body fat or distribution.
# It is widely used in public health and clinical settings as a quick and simple tool to assess potential health risks associated with weight. 
# Different BMI ranges are associated with different health categories, but it's important to note that BMI has limitations and does not account for factors such as muscle mass or distribution of fat
###############################################
def bodymassindex(height_cm, weight):
    height_m = height_cm / 100 
    return round((weight / height_m**2), 2)

h = float(input("Enter your height in centimeters: "))
w = float(input("Enter your weight in kg: "))

print("--------------------------Welcome to the BMI calculator--------------------------")
bmi = bodymassindex(h, w)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight⏬")
elif 18.5 <= bmi <= 24.9:
    print("Your weight is normal👌")
elif 25 <= bmi <= 29.9:
    print("You are overweight⏫")
else:
    print("You are obese⛔")
