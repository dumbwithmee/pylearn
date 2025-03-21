# 연습문제 4.1 4.2
def get_real(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("유효한 숫자를 입력하세요.")

fahrenheit = get_real("변환하고자 하는 화씨 온도?: ")

def fahrenheit_to_celsius(fahrenheit):
    return 5/9 * (fahrenheit - 32)

celsius = fahrenheit_to_celsius(fahrenheit)
print(f"화씨 {fahrenheit:1f}도는 섭씨 {celsius:.10f}°C")
