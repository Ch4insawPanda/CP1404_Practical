import random
print(random.randint(5, 20))  # line 1
#A number between 5 and 20, both being inclusive was printed.
#The smallest number you could see was 5 while largest was 20.
print(random.randrange(3, 10, 2))  # line 2
#The numbers 3, 5, 7 and 9 were generated randomly.
#The smallest number you could see was 3 while largest was 9.
#No, it can't.
print(random.uniform(2.5, 5.5))  # line 3
#A random float between 2.5 and 5.5 was produced.
#The smallest number you could see was 2.5 with the largest being 5.5, but both are very unlikely to come out.
print(random.randint(1, 100))
