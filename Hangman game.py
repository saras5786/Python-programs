word = "cat"
guessed = ""
chances = 5

print("Guess the word!")

while chances > 0:
    display = ""
    
    for ch in word:
        if ch in guessed:
            display += ch
        else:
            display += "_"
    
    print(display)

    if display == word:
        print("You won!")
        break

    guess = input("Enter a letter: ")

    if guess not in word:
        chances -= 1
        print("Wrong guess!")

    guessed += guess

if chances == 0:
    print("You lost! Word was:", word)
