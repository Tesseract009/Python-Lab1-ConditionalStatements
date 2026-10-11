import bmi
import zodiac
import birthday

while True:
    print("Welcome to Python Lab 5! This repository includes 3 applications. \n Press 1 for **BMI Calculator** \nPress 2 for **Zodiac Determiner** \n Press 3 for **Birthday Guesser** \n Press 4 to exit.")
    try: 
        ans = int(input())
    except ValueError:
        continue
    if ans == 1:
        bmi.run()
    if ans == 2:
        zodiac.run()
    if ans == 3:
        birthday.run()
    if ans == 4:
        print("Thanks for checking my assignments out. Goodbye!")
        break

    
    
