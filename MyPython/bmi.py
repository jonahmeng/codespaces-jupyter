weight = int(input('What is your weight (kg): '))

height = int(input('What is your height (cm): '))

bmi = weight / ((height/100) * (height/100))

print(f'BMI value: {bmi:.1f}')