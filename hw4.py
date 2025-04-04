def rep_char(c,n) :
    print(c*n)

def draw_line_string(msg):
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print('input his/her name : ',msg)
    rep_char('-',nstr)
    print(f'Hello, {msg}')
    print('Welcome to Seoul')
    rep_char('-',nstr)


m1 = input('input his/her name1 : ')
draw_line_string(m1)