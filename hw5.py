# 세 자리수 이하의 10진 정수 하나를 입력받아
# 다음과 같이 각 자릿수를 한글로 읽어주는 프로그램 작성
# 임의의 한 자리 10진 정수에 대한 한글 문자열을 화면상에 출력하는
# 함수 read_single_digit() 작성
# ▪ 임의의 세 자리 10진 정수에 대한 한글 문자열 출력을
# read_single_digit() 호출을 통해 처리하는 함수 read_number() 작성
# ▪ 주 프로그램부에서는 위 두 함수를 이용해 입출력 처리 담당

# 선언
def read_single_digit(num) :
    if num == 0 :
        print("영", end=" ")
    elif num == 1 :
        print("일", end=" ")
    elif num == 2 :
        print("이", end=" ")
    elif num == 3 :
        print("삼", end=" ")
    elif num == 4 :
        print("사", end=" ")
    elif num == 5 :
        print("오", end=" ")
    elif num == 6 :
        print("육", end=" ")
    elif num == 7 :
        print("칠", end=" ")
    elif num == 8 :
        print("팔", end=" ")
    else :
        print("구", end=" ")

def read_number(num):
    if num < 10:
        print(read_single_digit(num))
    elif num < 100:
        tens = num // 10
        ones = num % 10
        read_single_digit(tens)
        read_single_digit(ones)
    else:
        hundreds = num // 100
        tens = (num % 100) // 10
        ones = num % 10
        read_single_digit(hundreds)
        read_single_digit(tens)
        read_single_digit(ones)

# 주프로그램부
num = int(input("세 자리 정수 입력 : "))
if num <= 999 :
    read_number(num)
else :
    print("3자리수만 입력해주세요")
