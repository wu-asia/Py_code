# mylist = [21, 25, 21, 23, 22, 20]
#
# mylist.append(31)
#
# mylist.extend([29, 33, 30])
#
# num1 = mylist[0]
#
# id = mylist.index(30)
# print(id)

def list_while_func():
    my_list = [22, 33, 44]
    id = 0
    while id < len(my_list):
        print(my_list[id])
        id += 1

def list_for_func():
    my_list = [22, 3,31, 2]
    for i in range(0, len(my_list)):
        print(my_list[i])


def list_for_func1():
    a = [1, 23, 4, 5]
    for i in a:
        print(i)


list_while_func()
list_for_func1()
list_for_func()