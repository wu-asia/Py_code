def factorial(x):
    ret = 1
    for i in range(1, x + 1):
        ret *= i
    return ret
#c(n, i) = n!/i! * (n - i)!
def c(n, i):
    ret = int(factorial(n)/(factorial(i)*factorial(n - i)))
    return ret

print(c(10, 1))