# Exercises: Level 3

#     Here we have a person dictionary. Feel free to modify it!

#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

#     Asabeneh Yetayeh lives in Finland. He is married.

person = {
  'first_name': 'Nasr',
  'last_name': 'Aroyehun',
  'age': 100,
  'country': 'Finland',
  'is_marred': False,
  'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address': {
      'street': 'Space street',
      'zipcode': '02210'
  }
}

if (person.get('skills')):
  midIndex = len(person['skills']) // 2
  print(person['skills'][midIndex])

  print('He has Python skills') if 'Python' in person['skills'] else print('He lacks Python skills')

frontend = ['JavaScript', 'React']
backend = ['Node', 'Python', 'MongoDB']
fullstack = ['React', 'Node', 'MongoDB'] 
if all(skill in person['skills'] for skill in frontend):
  print('He is a front end developer')
elif all(skill in person['skills'] for skill in backend):
  print('He is a backend developer')
elif all(skill in person['skills'] for skill in fullstack):
  print('He is a fullstack developer')
else:  print('Unknown title')

if person['is_marred'] and person['country'] == 'Finland':
  print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
