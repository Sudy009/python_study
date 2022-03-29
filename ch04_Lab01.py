#chapter04 Lab: 어떤 종류의 학생인지 맞히기
print("당신이 태어난 연도를 입력하세요.")
year = int(input())     #입력받는 경우 자료형 지정해주
age = (2020 - year + 1)
#논리연산자 없이 비교연산자 사용 가능하지만 좋은 코드는 아님
if 20<= age <=26:
    print("대학생")
elif 17<= age <20:
    print("고등학생")
elif 14<= age <17:
    print("중학생")
elif 8<= age <14:
    print("초등학생")
else:
    print("그 외의 경우는 학생이 아닙니다.")
