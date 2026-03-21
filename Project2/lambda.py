def test_func(compute):
    result = compute(1, 2)
    print(f'result is {result}')

def add(x, y):
    return x + y
test_func(lambda x, y: x + y)