def add(a, b):
    # 두 수를 더합니다.
    return a + b


def substract(a, b):
    # 첫 번째 수에서 두 번째 수를 뺍니다.
    return a - b


def multiply(a, b):
    # 두 수를 곱합니다.
    return a * b


def divide(a, b):
    # 두 수를 나누며, 0으로 나누면 예외를 발생시킵니다.
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


def main():
    # 두 숫자와 연산자를 입력받아 결과 또는 안내 메시지를 출력합니다.
    try:
        a = float(input("첫 번째 숫자: "))
        b = float(input("두 번째 숫자: "))
    except ValueError:
        print("올바른 숫자를 입력해 주세요.")
        return

    operator = input("연산자 (+, -, *, /): ").strip()
    operations = {"+": add, "-": substract, "*": multiply, "/": divide}
    if operator not in operations:
        print("연산자는 +, -, *, / 중 하나를 입력해 주세요.")
        return

    try:
        result = operations[operator](a, b)
    except ValueError as error:
        print(error)
        return

    print(f"결과: {result}")


if __name__ == "__main__":
    main()
