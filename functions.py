def unlimted_arguments(*args):    # As many arguments we want
    print('args', args)


unlimted_arguments(1,2,3,4)

unlimted_arguments(*[1,2,3,4]) # comma separted values is reached

numbers = [1,2,3]
text = 'This is number {}{}'.format(*numbers)

print(text)

def namedArguments(*args, **keywords):
    print(keywords) # keywords store named arguments
    print(args)

namedArguments(1,2,3,4,name='Dash',age='29')