def rep_char(c, n):
    print(c * n)

def draw_line_string(name):
    print(f'input his/her name : {name}')
    rep_char('--', len(name))
    print(f'Hello, {name}')
    print('Welcome to Seoul')
    rep_char('----', len(name))
    print()  # 줄 바꿈

# 주 프로그램
m1 = input('input his/her name1 : ')
m2 = input('input his/her name2 : ')
draw_line_string(m1)
draw_line_string(m2)