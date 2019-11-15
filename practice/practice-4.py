def normal(argument, *args):
    for arg in args:
        print('Result is {:^20}'.format(argument(arg)))

normal(lambda data: data/5,12,3,4,45)

