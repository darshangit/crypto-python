import copy

person = [{'name': 'Dash', 'age': 29, 'hobbies': ['dance', 'sing']},
{'name': 'Priya', 'age': 21, 'hobbies': ['fighting', 'sing']},
{'name': 'arjun', 'age': 30, 'hobbies': ['fighting', 'dance']}]

person_names =  [el['name'] for el in person]

all_are_older_than_20 = all(el['age'] > 20 for el in person)

shallow_copy_persons = person[:]
shallow_copy_persons[0]['name'] = 'ppp'

print('shallow_copy_persons',shallow_copy_persons)
print('person',person)

deep_copy = copy.deepcopy(person)
deep_copy[0]['name'] = 'DASH'

a, b, c = person

print('----------------' * 20)

print(a, b, c)

print('  ' * 20)

print('person', person)
print('deepcopy', deep_copy)

print('----------------' * 20)

print('person_names', person_names)

print('----------------' * 20)

print('all_are_older_than_20', all_are_older_than_20)