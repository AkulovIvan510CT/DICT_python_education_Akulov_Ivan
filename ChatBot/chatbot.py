print("Hello! My name is DICT_Bot.")
print("I was created in 2020.")
print("Please, remind me your name")

name_input = input("> ")

print("What a great name you have,", name_input)
print("Let me guess your name")
print("Enter remainders of diving you age by 3,5 and 7")

remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is ", age)
print("that's a good time to start programming!")
print("Now I will prove to you that i can count to any number you want")

number_input = int(input("> "))

custom_number = 0

while custom_number <= number_input:
    print(custom_number,"!")
    custom_number = custom_number+1

print("Completed, have a nice day!")
print("Let's test your programming knowledge")
print("Why do we use methods?")
print("1. To repeat a statement multiple times")
print("2. To decompose a program into several small subroutines")
print("3. To determine the execution time of a program")
print("4. To interrupt the execution of a program.")

count_input = int(input("> "))

while count_input != 2:
    print("Please, try again")
    count_input = int(input("> "))

print("Congratulations, have a nice day!")
