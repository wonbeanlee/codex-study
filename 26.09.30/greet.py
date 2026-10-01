# utils.py에서 인사말을 만드는 함수를 가져옵니다.
from utils import make_greetings


# 이름을 입력할 때까지 반복해서 물어봅니다.
while True:
    # input()으로 이름을 입력받고, strip()으로 앞뒤 공백을 없앱니다.
    name = input("이름을 입력하세요: ").strip()

    # 이름이 비어 있으면 안내하고 다시 입력받습니다.
    if name == "":
        print("이름을 입력해주세요")
    else:
        # 이름이 입력되면 break로 반복을 끝냅니다.
        break

# 함수가 만든 두 인사말을 각각 변수에 저장하고 화면에 출력합니다.
korean_greeting, english_greeting = make_greetings(name)
print(korean_greeting)
print(english_greeting)
