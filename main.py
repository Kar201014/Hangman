import random

from hangman_words import word_list
from hagman_art import logo
from hagman_art import stages
print(logo)

chosen_word = random.choice(word_list)
word_laght = len(chosen_word)

end_of_game = False
lives = 6

# while end_of_game:
#      x = input("greg tary")
#      if x == chosen_word
#      print(x)
# else:
displey = []
for _ in range(word_laght):
     displey += "_"
     
while not end_of_game:
     guess = input("Asa tar ").lower()
     
     if guess in displey:
         print(f"asel es arden ayd tary {guess}")
         
     for position in range(word_laght):
         letter = chosen_word[position]
         if letter == guess:
            displey[position] = letter
     if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a live")
        
        lives -= 1
        if lives == 0:
           end_of_game = True
           print("You lose.")
     print(f"{''.join(displey)}")
     
     if "_" not in displey:
            end_of_game = True
            print("You win")
            
     print(stages[lives])                                          
        
        
