def input_positive_number(prompt):
    n=0
    while n<=0:
        n= int(input(prompt))
    return n


def display_multiplication_table(n):
    for i in range(1,10):
        print(f"{n} x {i} = {n * i:2d}")

def display_multiplication_table(n):
    i=1
    while i<=9:
        print(f"{n} x {i} = {n * i:2d}")
        i+=1

n = input_positive_number('출력할 구구단을 입력해주세요')

display_multiplication_table(n)