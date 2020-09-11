a = set('hello')
print(type(a))
print(a)

b = {23, '32'}
print(type(b))
print(b)

c = frozenset('Qwerty')  # can not change this, but 'set' can change

n = ['a', 'a', 'v', 4, 4, 5, 8]
print(n)
print(set(n))

m = {32, 45, 43.23, 79}
x = 55
print(x in m)  # operator 'in' check that variable = 'x' locate in m

k = {32, 45, 43.23, 79}
l = {55, 896}
print(k.isdisjoint(l))  # check that at least one element coincides

s = {32, 45, 43.23, 79}
d = {55, 896, 45, 32}
s.update(d)  # join 2 sets, and return set with unique element
print(s)

f = {32, 45, 43.23, 79}
g = {55, 896, 45, 32}
f.intersection_update(g)  # return set with elements which are in both sets
print(f)

h = {32, 45, 43.23, 79}
j = {55, 896, 45, 32}
h.difference_update(j)  # return set in which are elements from 'h', but these elements are not in 'j'
print(h)