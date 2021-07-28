for i in range(1, 21, 2):   #copied from github practical
    print(i, end=' ')
print()

#for part a
for i in range(0, 101, 10):   #for counting in 10s from 0 to 100
    print(i, end=' ')
print()

#for part b
for i in range(20, 0, -1):    #for counting loop in descending order from 20 to 1
    print(i, end=' ')
print()

#for part c
NumOfStars = int(input("Enter Number of Stars: "))
for i in range (NumOfStars):
    print('*', end='')

#for part d
NumOfStars = int(input("\nEnter Number of Stars: "))
for i in range (NumOfStars):
    for j in range(i+1):
        print('*', end='')
    print()