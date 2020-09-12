file = open('text.txt', 'w')

file.write('Hi it is me\nteradek asap')

file.close()

file = open('text.txt')

#  print('print file contents: ' + file.read())

for line in file:
    print(line)

file.close()
