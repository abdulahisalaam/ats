import random
def get_word():
    with open('words.txt', 'r') as f:
        words = f.readlines()
    word = [char for char in words]
    return word

def return_random():
    a=get_word()
    random.choice(a)
    return random.choice(a)

def input_char():
    return input('Enter a character to check the guess word from computer: ')

def game_now():
    guess=input_char()
    word = return_random()

    if guess in word:
        n = 8
        while n >= 8:
            print(f"your Guess is '{guess}'")
            print(word)    
            w = []
            for b in word:
                for a in b:
                    if a == guess:
                        w.append(a)
                    elif not a == guess:
                        w.append(b.replace(a, '_'))
            z =''.join(w)
                   
            return f': {z}'
        else:
            return f"'{guess}' not found in '{word}' try again. \n\t ________"
    return f' {z}'
        
if __name__ == '__main__':
    print(game_now())


