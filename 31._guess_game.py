import random
def randomm():
    return random.randint(1,11)
def guess_a_number():
    return int(input('Guess a number: '))

def guess_game():
    n = 5
    while n <= 5:
        return guess_a_number()
    if guess_a_number() == randomm():return 'You Won Computer!'
    elif guess_a_number():return 'Computer Won!'


            

if __name__== '__main__':
    print(guess_game())
   