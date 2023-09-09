
print("A ______ doctor was ______ to operate a person as there was ______. ")
print("Find that one word which fills all 3 blanks.")

secret_word = "notable"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You Lose!")
else:
    print("You Win!")
