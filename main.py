import random
import names
import art
import os

#Variables
lives = 6
chosen_word = random.choice(names.arsenal_players)
display = []
word_length = len(chosen_word)
end_of_game = False




print("Welcome to Arsenals Hangman!")
for letter in range(word_length):
    display += "_"
print(display)

while not end_of_game and lives > 0:
  guess = input("Guess the letter: ").lower()
  # Clear the terminal screen
  os.system('clear' if os.name == 'posix' else 'cls')
  if guess in display:
    print(f"You've already guessed {guess}")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life. ")
    lives -= 1
    print(art.stages[lives])
  print(display)
  if "_" not in display:
    end_of_game = True
    print('You win "Gunner"!')
  elif lives == 0:
    print("Game over.")
    print("Watch more football, brah...")
