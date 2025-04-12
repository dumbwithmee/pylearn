def rep_char(c, n):
    print(c * n)


def draw_line_string(msg1, msg2):
    nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)

    print('input his/her name :', msg1)
    rep_char('-', nstr)
    print(f'Hello, {msg1}')
    print('Welcome to Seoul')
    rep_char('-', nstr)


# 주 프로그램
m1 = input('input his/her name1 : ')
m2 = input('input his/her name2 : ')
draw_line_string(m1, m2)
