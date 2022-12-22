import random
import hangman_art
import hangman_words
from replit import clear

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print("The letter "+ guess + " is already been guessed")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        
        print("The letter "+guess+" is not in the word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print("The Correct Answer is "+chosen_word)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win, The answer is "+ chosen_word)

    print(hangman_art.stages[lives])
