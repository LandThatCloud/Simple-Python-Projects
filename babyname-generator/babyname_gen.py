import random,string

letter_input_1 = input('For consonants press "c", vowels "v" and other letters "l"')
letter_input_2 = input('For consonants press "c", vowels "v" and other letters "l"')
letter_input_3 = input('For consonants press "c", vowels "v" and other letters "l"')
letter_input_4 = input('For consonants press "c", vowels "v" and other letters "l"')
letter_input_5 = input('For consonants press "c", vowels "v" and other letters "l"')

consonants = 'bcdfghjklmnpqrstvwxz'
vowels = 'aeiouy'
letters = string.ascii_lowercase


def generator():
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = letter_input_1

    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = letter_input_2

    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = letter_input_3

    if letter_input_4 == 'v':
        letter4 = random.choice(vowels)
    elif letter_input_4 == 'c':
        letter4 = random.choice(consonants)
    elif letter_input_4 == 'l':
        letter4 = random.choice(letters)
    else:
        letter4 = letter_input_4

    if letter_input_5 == 'v':
        letter5 = random.choice(vowels)
    elif letter_input_5 == 'c':
        letter5 = random.choice(consonants)
    elif letter_input_5 == 'l':
        letter5 = random.choice(letters)
    else:
        letter5 = letter_input_5

    name = letter1+letter2+letter3+letter4+letter5

    return name


for babynames in range(20):
    print(generator())

