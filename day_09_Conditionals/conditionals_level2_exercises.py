# Exercises: Level 2

#     Write a code which gives grade to students according to theirs scores:

#     80-100, A
#     70-89, B
#     60-69, C
#     50-59, D
#     0-49, F

def grade(score):
  if score >= 80 and score <= 100:
    return 'A'
  elif score >= 70 and score <=79:
    return 'B'
  elif score >= 60 and score <= 69:
    return 'C'
  elif score >= 50 and score <= 59:
    return 'D'
  elif score >= 0 and score <= 49:
    return 'F'
  else:
    return 'Invalid'
score = int(input("Enter exam score (0 - 100): "))
print(f"{score} is a {grade(score)}")
  

#     Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

## Get month from the user 
month = input("Enter month: ").capitalize()
season = ''

if month in autumn:
  season = 'Autumn'
elif month in winter:
  season = 'Winter'
elif month in spring:
  season = 'Spring'
elif month in summer:
  season = 'Summer'
else:
  print('Invalid month')

print(f"The season is {season}")


#     The following list contains some fruits:

# ```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
# ```

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input("Add a fruit: ").lower() # prevent same fruit written in different cases from being added to the list

if fruit in fruits:
  print("That fruit already exists in the fruits list")
else:
  fruits.append(fruit)
  print(fruits)