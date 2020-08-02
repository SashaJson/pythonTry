def func (a, b):
    res = a + b
    return res

print(func(25, 25))

def func1 (a):
    def add (x):
        return a + x
    return add

test = func1(100)
print(test(200))

def func2 ():
    pass

print(func2())

def func3 (a, b, c = 2):
    res = a + b
    res += c
    return res

print(func3(2, 2))

def func4 (*arg):
    return arg

print(func4(25, 85, 'asap'))

def func5 (**arg):
    return arg

print(func5(a = 55, b = 'asa[g'))

test2 = lambda x, z: x + z
print(test2(5, 5))

print((lambda a, b: a * b)(10, 10))