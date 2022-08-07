from collections import Counter


def generate_phrase(characters, phrase):
    if Counter(characters) == Counter(phrase):
        print('True')
    else:
        print('False')


generate_phrase('cbacba', 'aabbccc')
generate_phrase('abc', 'cabb')