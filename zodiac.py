def run():
  while True:
    try: 
      year = int(input("Enter your birth year: "))
      break
    except ValueError:
      print("Please enter a number")
      continue
  zodiac_list = ("Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig")
  zodiac = (year - 1900) % 12
  print(f"Your Chinese zoidac sign is {zodiac_list[zodiac]}")