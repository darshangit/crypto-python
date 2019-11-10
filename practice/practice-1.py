def print_as_a_string(age=22, name='Dash'):
    print(name + ' ' + str(age))


print_as_a_string()


def number_of_decades_lived(age=32):
    print('Number of Decades Lived', age / 10)


number_of_decades_lived(int(input('Enter Your Age: ')))
