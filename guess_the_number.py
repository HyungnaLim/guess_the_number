import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
guesses = 0


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    global guesses
    if guess == secret:
        guesses += 1
        return correct
        
    if guess < secret:
        guesses += 1
        return too_low
        
    if guess > secret:
        guesses += 1
        return too_high
    
    


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print('Thanks for playing the game!')
    print(f'You guessed {guesses} times')


if __name__ == '__main__':
    main()
