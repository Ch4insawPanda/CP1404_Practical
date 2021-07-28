#1
out_file = open('name.txt', 'w')

Name = input("Enter Name :")
print(Name, file=out_file)

out_file.close()

#2
in_file = open('name.txt', 'r')

for line in in_file:
    print('Your name is {}'.format(line))

in_file.close()

#3
in_file = open('numbers.txt', 'r')

line_one = in_file.readline()
line_two = in_file.readline()
number_one = int(line_one)
number_two = int(line_two)
print('{0:>3}+{1}={2}'.format(number_one,number_two,number_one+number_two))

in_file.close()

#4
in_file = open('numbers.txt','r')

modified_list = []
number_list = in_file.readlines()
for i in range(len(number_list)):
    Line = number_list[i]
    number = int(Line)
    modified_list.append(number)
print(modified_list)
print('{:7}'.format(sum(modified_list)))

in_file.close()
