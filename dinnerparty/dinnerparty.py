import random

human_dict = {}
person_input = int(input("Input number person: "))

if person_input <= 0:
    print("No one is join for the party.")
else:
    for i in range(person_input):
        name_input = input("Enter name: ")
        human_dict[name_input] = 0

    print("Enter the total amount.")
    total_amount_input = int(input())

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ")
    write = input()

    names_list = list(human_dict.keys())

    if write == "Yes":
        random_person = random.choice(names_list)
        print(random_person, " is the lucky one!")
        person_input -= 1
        amount_sharing = total_amount_input/person_input
        for i in range(len(names_list)):
            var = names_list[i] == random_person
            human_dict[names_list[i]] = "%.2f" % amount_sharing
            human_dict[random_person] = 0
    else:
        print("No one is going to be lucky.")
        amount_sharing = total_amount_input / person_input
        for i in range(len(names_list)):
            human_dict[names_list[i]] = "%.2f" % amount_sharing

print(human_dict)
