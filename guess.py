from random import randrange

print "Hey playa playa"

name = raw_input("WHat is your name? ")

print "Hello %s! I'm thinking of a number between 1 and 100. Try to guess my number." % name

answer = randrange(1, 101)

while True:
    guess = int(raw_input("Your guess? "))
    if guess < answer:
        print "Your guess is too low."
    elif guess > answer:
        print "Your guess is too high."
    else:
        print "Good job!"
        break
