import random

with open('wordlist.txt', 'r') as f:
  words = f.readlines()
  logo = (
        """
      HH   HH     AAA     NN   NN   GGGG
      HH   HH    AAAAA    NNN  NN  GG  GG
      HHHHHHH   AA   AA   NN N NN GG     
      HH   HH  AAAAAAAAA  NN  NNN GG   GG
      HH   HH AAA     AAA NN   NN  GGGGGG
        """
     """
      MM    MM     AAA     NN   NN
      MMM  MMM    AAAAA    NNN  NN
      MM MM MM   AA   AA   NN N NN
      MM    MM  AAAAAAAAA  NN  NNN
      MM    MM AAA     AAA NN   NN
        """
       """
        GGGG       AAA     MM    MM EEEEE
       GG  GG     AAAAA    MMM  MMM EE
      GG         AA   AA   MM MM MM EEEE
      GG   GG   AAAAAAAAA  MM    MM EE
       GGGGGG  AAA     AAA MM    MM EEEEEE
       """
       
  )
  print(logo)

word = random.choice(words)[:-1]

allowed_errors = 13
guesses = []
done = False

while not done:
  for letter in word:
    if letter.lower() in guesses:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print("")

  guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
  guesses.append(guess.lower())
  if guess.lower() not in word.lower():
    allowed_errors -= 1
    if allowed_errors == 0:
      break

  done = True
  for letter in word:
    if letter.lower() not in guesses:
      done = False

if done:
  print(f"You found the word! It was {word}!")
  win = ("GRATE, YOU WIN!!!\nWANT ONE MORE TIME TO PLAY PRESS RUN!")
  print(win)
else:
  print(f"Game Over! The word was {word}!")
  lives_left = (
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """
  )
  print(lives_left)