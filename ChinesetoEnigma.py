from __future__ import unicode_literals
from random import randint

while True:
    chinese = input('请输入中文：    ')
    enigma = ''


    def get_random_number(digit_length):
        random_number = ''
        for _ in range(digit_length):
            random_number += str(randint(0, 9))
        return random_number

    for hans in chinese:
        enigma += '321' + str(ord(hans))

    enigma = int(enigma)
    # print(enigma)
    english = ''
    i = 0
    key = True
    while enigma:
        i += 1
        if key:
            english += chr(enigma % 26 + 97).upper()
            key = False
        else:
            english += chr(enigma % 26 + 97)
        enigma //= 26
        if enigma:
            if randint(3, 8) < i and enigma > 1000:
                if randint(1, 7) == 2:
                    english += '.'
                    key = True
                english += ' '
                i = 0
    print('Enigma码是：    ', english + '.')