'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells
them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)

Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)'''
print('Enter your name: ')
name = str(input())
print('Enter your age: ')
age = int(input())

years_before_100 = 100 - age

print('Has your birthday happened yet this year? Yes = 1 No = 0')
b_day = int(input())

print('Enter number of desired repeated message: ')
copies_of_message = int(input())

if b_day == 1: years_before_100 = years_before_100 - 1

year_of_100 = 2021 + years_before_100

message_num = 0
while message_num < copies_of_message:
    print(name + ', you will turn 100 years old in the year', year_of_100)
    message_num += 1