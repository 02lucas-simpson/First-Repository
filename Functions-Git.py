# Lucas Simspon
# 2.6.19
# 4.13.3: Greating


name = input("What is your name: ")

def greeting():
    print ("Hi there " + name + "!")
    print ("Nice to meet you!")

greeting()


#4.13.4: Functions and Variables
#Lucas Simpson
#2.14.19

x = 11

def print_something():
    x = 69
    print (x)

print_something()
print(x)


# 4.13.5: Functions and Variables - Part 2
# Lucas Simpson
# 2.14.19

my_variable = 3.6846

def something():
    print(my_variable + 10 )

something()

# 4.13.6: Functions & variables, Part 3
# Lucas Simpson
# 2.18.19

def print_number(bekfist):
    print(str(bekfist))

print_number(13)
print_number('\n' + 'Hello bekfist')

# 4.14.4: Name & Age
# Lucas Simpson
# 2.18.19

def name_and_age(name, age):

    print('\n''Hi, my name is what? My name is who? My name is',name,'and i am',str(age),'years old')

name_and_age('silca slica slim shady',46)
name_and_age('Dr. Seuss',74)
name_and_age('Dr.Dre',63)

# 4.14.5: Default Parameter Values
# Lucas Simpson
# 2.19.19

def print_two_numbers(x, y = 20):
    print('First number: ', x)
    print('Second number: ', y)

print_two_numbers(5, 67)
print_two_numbers(23)


# 4.14.7: Print Multiple times
# Lucas Simpson
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)


print_multiple_times('suh suh g', 4)


# 4.14.7: Print Multiple times
# Lucas Simpson
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)


print_multiple_times('suh suh g', 4)

