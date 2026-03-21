d1 = {'first':99, 'second':88, 'third':77}
#print(d1)
#print(d1['first'])

d2 = {'first':{'one':99, 'two':88, 'three':77},
      'second':{'one':66, 'two':55, 'three':44},
      'third':{'one':33, 'two':22, 'three':11}}

d1_keys = d1.keys()
print(type(d1_keys))
print(d1_keys)
d2_keys = d2.keys()
print(d2_keys)
d2_first_keys = d2['first'].keys()
print(d2_first_keys)

for i in d1_keys:
      print(f'{i} : {d1[i]}')


