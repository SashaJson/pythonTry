d = {'test': 1, 'test_2': 'Asapp'}
print(d['test_2'])
print(d)
d['test'] = 2
print(d)

c = dict(short='dict', longer='dictionary')
print(c)
c['short'] = 666
print(c)

v = dict([(55, 44), (99, 155)])
print(v)
v[55] = 88888
print(v)

n = dict.fromkeys(['a', 'b', 'c'])
print(n)
m = dict.fromkeys(['a', 'b', 'c'], 1)
print(m)

d = {a: a ** 2 for a in range(7)}
print(d)

