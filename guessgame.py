secret_word="ignite"
guess=""
guess_count=0
out_of_guess=False
while guess!=secret_word and not(out_of_guess):
    if guess_count <3:
        guess=input("Enter guess: ")
        guess_count+=1
    else:
        out_of_guess=True
if out_of_guess:
  print("out_of_guesses! YOU LOSE")
else:
   print("YOU WIN!")
