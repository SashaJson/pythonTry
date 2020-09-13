def decorator(func):
    def wrapper():
        print('1')
        func()
        print('2')
    return wrapper

@decorator
def show():
    print('Hello world')


#  dec = decorator(show)
show()