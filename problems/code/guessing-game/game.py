import random

low, high = 1, 100
tries = 10

answer = random.randint(low, high)
print("I'm thinking of a number between %d and %d." % (low, high))

for i in range(tries):
    raw_guess = raw_input("[%2d] Your guess: " % (tries-i))
    guess = int(raw_guess)
    if guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    else:
        print("Congratulations, you got it!")
        exit()

print("Sorry, the answer was %d. Better luck next time." % answer)
