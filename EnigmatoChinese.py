from __future__ import unicode_literals
while True:
    english = input('请输入Enigma码：    ').lower()
    enigma = 0
    j = 0
    for i in english:
        if i != ' ' and i != '.':
            # print(i)
            enigma += (ord(i)-97) * 26 ** j
            j += 1
    # print(enigma)
    try:
        chinese = ''.join([chr(int(x)) for x in str(enigma).split('321') if x])
        print('中文是：    ', chinese)
    except OverflowError:
        print('Enigma语法错误！')



