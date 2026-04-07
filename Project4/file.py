f = open('hello.txt', 'r', encoding = 'UTF-8')

print(type(f))

# print(f.read(12))
#
# print(f.read(11))

# line = f.readlines()
# print(type(line))
# print(line)

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

for e in f:
    print(e)

f.close()