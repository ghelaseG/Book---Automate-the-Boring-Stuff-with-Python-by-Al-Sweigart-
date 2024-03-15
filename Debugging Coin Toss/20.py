import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)a - '
                    '%(levelname)s - %(message)s')

logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of guess')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug('Start of coin toss')
toss = random.randint(0,1) #0 is tails, 1 is heads

if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'

logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program!')
