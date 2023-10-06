hint = ['_', '_', '_', '_', '_', '_']
hint_result = ' '.join(hint) 

secret = "mosiah"
guess_count = 0

print("Welcome to the word guessing game!")

print(f"Your hint is:{hint_result}")
guess_word = input("What is your guess? ")

while (secret != guess_word):
   if (len(secret) != len(guess_word)):
      print()
      print("Sorry, the guess must have the same number of letters as the secret word.")
      guess_word = input("What is your guess? ")
   else: 
      for i in range(len(secret)):
         for j in range(len(guess_word)):
            # print(f"{i} - {j}"")
            # print(f"{guess_word[i]} - {secret_word[j]})
            if (list(guess_word)[i] == list(secret)[j]):
               hint[i] = guess_word[i]
               hint_result = " ".join(hint)
      guess_count = guess_count + 1
      print(f"Your hint is: {hint_result}")
      guess_word = input("What is your guess? ")
print(f"It took you {guess_count} guesses")
print("Thank you for playing. Goodbye.")
