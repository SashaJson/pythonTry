l = [12, 55, 'asap', 88]

i = 0
while i < 4:
    print(l[i])
    i += 1

print(l[:])  # [12, 55, 'asap', 88]
print(l[1:])  # [55, 'asap', 88]
print(l[:1])  # [12]
print(l[::2])  # [12, 'asap']
