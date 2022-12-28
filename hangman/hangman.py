import random  # импортированая функция

while True:

    print("Type play to play the game, exit to quit:> ")
    action = ("play", "exit")
    user_input = input()

    while user_input != "play" and user_input != "exit":
        print("Write some action:> ")
        user_input = input()

    if user_input == "play":

        print("HANGMAN")
        print("The game will be available soon")

        word_tuple = ('python', 'java', 'javascript', 'php')
        random_ask = random.choice(word_tuple)
        cipher = ['-'] * len(random_ask)

        print("Guess the word", cipher, ":> ")

        chance = 8
        letter = []

        while chance > 0 and ''.join(
                cipher) != random_ask:  # ''.join() Метод join()берет все элементы в итерируемом объекте и объединяет
            # их в одну строку.

            word_input = input()

            if word_input != word_input.lower():
                print("Please enter a lowercase English latter.")
                continue

            if len(word_input) > 1:
                print("You should input a single letter.")
                continue

            if word_input in letter:
                print("You`ve already guessed this letter.\nLeft ", chance,
                      " chance.")  # n - переход на следующую строку.
                continue

            if word_input in letter:
                print("You`ve already guessed this letter.\nLeft ", chance, " chance.")
                continue

            letter.append(word_input)

            if word_input in random_ask:
                for i in range(len(random_ask)):
                    if random_ask[i] == word_input:
                        cipher[i] = word_input
                print(cipher)
            else:
                chance -= 1
                print("That letter doesn't appear in the word.")
                print("left ", chance, " chance.")
                print("Guess the word", cipher, ":> ")

        if chance == 0:
            print("\nYou lost!\n")
        else:
            print("\nYou survived!\n")

    if user_input == "exit":
        break
