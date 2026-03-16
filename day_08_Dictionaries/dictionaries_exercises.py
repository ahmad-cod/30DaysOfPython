# Day 08: 30 Days of Python Programming
# Create an empty dictionary called dog
dog = dict()
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Jack'
dog['color'] = 'Brown'
dog['breed'] = 'german shepherd'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
  'first_name': 'Sadiq',
  'last_name': 'Ahmad',
  'gender': 'male',
  'age': 22,
  'marital_status': 'single',
  'skills': ['Quran Recitation', 'Mathematics'],
  'country': 'Nigeria',
  'city': 'Kano',
  'address': 'BUK New Site'
}
# Get the length of the student dictionary
print('Length of student dictionary:', len(student))

# Get the value of skills and check the data type, it should be a list
print('Skills:', student['skills'])
print('Data type of skills:', type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('Table Tennis')

# Get the dictionary keys as a list
print('Keys in the student dictionary:')
print(student.keys())

# Get the dictionary values as a list
print('Values in the student dictionary:')
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.popitem()
# Delete one of the dictionaries
del dog
# print(dog['name'])