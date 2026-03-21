my_set = {'hello', 'the', 'world', 'hello', 'the', 'world'}
print(my_set)
print(len(my_set))
print(type(my_set))

my_set.add('python')

print(my_set)

my_set.remove('python')

print(my_set)
my_set.pop()
print(my_set)
print('hello' in my_set)
print('world' in my_set)

#
# s1 = {'hello', 'the', 'world'}
# print(s1)
# print('python' in s1)
# print('hello' in s1)
# s1.add('python')
# print(s1)
# print('python' in s1)
# print('hello' in s1)