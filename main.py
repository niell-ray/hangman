import random as rand
import hangman_words as hang_words
import hangman_art as hang_art

lives = 6

print(hang_art.logo)
chosen_word = rand.choice(hangwords.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
  placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
  print(f"****************************<???>/{lives} LIVES LEFT****************************")
  guess = input("Guess the letter: ").lower()

  if guess in correct_letter:
    print(f"already typed {guess}")
  display = ""

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"

  print("Word to guess" + display)

if guess not in chosen_word:
  lives -= 1
  print(f"your guess is wrong, u lose a life.")
  if lives == 0:
    game_over = True

    print(f"***********************YOU LOSE, the word is {chosen_word}**********************")

if "_" not in display:
  game_over = True
  print("****************************YOU WIN****************************")

print(hang_art.stages[lives])
