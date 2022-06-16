import random


def print_time_no_repeat(num):

    sentence = ["He has ten cows.",
                "I have ten pens.",
                "I'll be back at ten.",
                "It's ten o'clock sharp.",
                "He speaks ten languages."
                ]

    for n in range(num):
        random.choice(sentence)
        value = set(sentence)
    return '\n'.join(value) 

print(print_time_no_repeat(3))



