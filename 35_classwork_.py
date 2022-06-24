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
        print(f"your Guess is '{guess}'")
        print(word)
        
        indx = [i for i, ltr in enumerate(word) if ltr == guess]
        indx_s = [i for i, ltr in enumerate(word) if not ltr == guess]
        al = [i for i in word]
        w = []
        for b in word:
            for a in b:
                if a == guess:
                    w.append(a)
                elif not a == guess:
                    w.append(b.replace(a, '_'))
                   
        return f' this is new b: {w}'

        print(indx_s)
        print(f"this word char {al}")
        print(f"this is replace {relpc}")
        return indx
    else:
       return f"'{guess}' not found in '{word}' try again. \n\t ________"

print(game_now())


