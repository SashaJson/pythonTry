lis = [1, 10, '5', 88, 'fff', [555, '78', 'dd']]
print(lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

b = [55, 189, 454, 6, 54]
l = []
l.append(20)  # add element in end list
l.extend(b)  # add in end list other list
l.insert(1, 888)  # add by index element in list
l.remove(55)  # delete element
l.pop(3)  # delete element by index
print(l.index(189))  # return index by element
print(l.count(20))  # how many items are in the list
l.sort()
l.reverse()
l.clear()

print(l)