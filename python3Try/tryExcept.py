try:
    x = int(input())
except ValueError:
    print('you input not a number')
    x = 0

try:
    y = int(input())
except ValueError:
    print('you input not a number')
    y = 0

try:
    res = x / y
except ZeroDivisionError:
    print('you input 0')
    res = 0
else:
    print('if try then execute')
finally:
    print('all try execute')

print(res)