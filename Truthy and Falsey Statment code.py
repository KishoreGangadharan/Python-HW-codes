#Codr for ruthy and falsey statements

name = ''
while not name:
    print('Enter your name:')
    name = input()
    print ('How many guest will you have?')
    numofguest = int(input())
    if numofguest:
        print ('Be sure to have enough rooms for all your guests')
    print ('Done')
