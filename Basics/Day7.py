#Hangman
import random
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                 
      ''')
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
result = []
word_len = len(chosen_word)
for i in range(word_len):
    result += "_"
max_tries = 0
while result.count("_") > 0 and max_tries < 6:
    guess = input("Guess a letter: ")
    if guess in result:
        print(f"You have already guessed {guess}")
    else:
        for l in range(word_len):
            if chosen_word[l] == guess:
                result[l] = guess
        if guess not in result:
            max_tries += 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(" ".join("{}".format(k) for k in result))
        print(HANGMANPICS[max_tries])
    
if "_" in result:
    print("Man has hanged!")
else:
    print("You Won!")