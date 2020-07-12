num = input('Enter number: ')

if int(num) > 0:
    print('You enter number more than 0')
    if int(num) > 10:
        print('You enter number more than 0 and 10')
        if int(num) > 20:
            print('You enter number more than 0, 10 and 20')
    else:
        print('You enter number less than 0, but no more - 20')
elif int(num) < -20:
    print('You enter number less -20')
else:
    print('You not ugly ;)')