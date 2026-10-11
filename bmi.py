def run():
    while True:
      try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        if weight <=0 or height<=0:
          print("Weight and height cannot be less than 0")
          continue
        break

      except ValueError:
        print("Please enter a number")
        continue
    bmi = round(weight / (height**2), 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you are normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are overweight.")
    else:
         print(f"Your BMI is {bmi}, you are obese.")
    