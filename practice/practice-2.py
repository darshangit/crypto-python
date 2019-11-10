list_of_names = ['Dash', 'prni', 'awesome']

for name_index in range(len(list_of_names)):
    name_length = len(list_of_names[name_index])
    current_name = list_of_names[name_index]
    if name_length > 5:
        print(list_of_names[name_index], 'Length : ', len(list_of_names[name_index]))
    if 'n' in current_name or 'N' in current_name:
        print('The name ' + current_name +  ' contains a n or N')

while len(list_of_names) > 0:
    print(list_of_names.pop())
else:
    print('List is empty')