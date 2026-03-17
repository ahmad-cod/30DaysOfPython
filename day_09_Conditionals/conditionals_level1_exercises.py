# Exercises: Level 1

#     Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#  inputs: age
#  mathematical model: if age >= 18: print('You are old enough to learn to drive.') else: print(f'You need {18 - age} more years to learn to drive.')

# age = int(input("Enter your age: "))
# print("You're old enough to drive.") if (age >= 18) else print(f"You need {18 - age} more years to learn to drive")

#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.

#     Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# my_age = 20
# print("Who is older (me or you)?")
# your_age = int(input("Enter your age: "))
# age_difference = abs(your_age - my_age)
# years_text = "years" if age_difference > 1 else "year"

# if your_age > my_age :
#   print(f"You're {age_difference } {years_text} older than me")
# elif your_age == my_age:
#   print("We're age mate.")
# else:
#   print(f"I'm {age_difference} {years_text} older than you.")

#     Enter your age: 30
#     You are 5 years older than me.

#     Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
number1 = int(input("Enter number one: "))
number2 = int(input("Enter number two: "))

if number1 > number2 :
  print(f"{number1} is greater than {number2}")
elif number1 < number2 :
  print(f"{number1} is smaller than {number2}")
else:
  print(f"{number1} is equal to {number2}")