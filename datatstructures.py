simple_list =[1,2,3,4]
simple_list.extend([5,6,7])
del(simple_list[0])
print(simple_list)

d = {'name': 'max'}
del(d['name'])
print(d.items())
for k, v in d.items():
    print(k, v)

t = (1,2,3)
print(t.index(3))

a = {'12', '2'}
a.discard('2')
print('a', a)

## All and Any

int_list = [1,2,3,4, -5]

pos_list = [el > 0 for el in int_list]
print(all(pos_list))
print(any(pos_list))