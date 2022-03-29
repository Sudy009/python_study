#if-elif-else문
score = int(input("Enter your score: "))

if score >=90:     #if문의 조건이 맞지 않으
    grade = 'A'
elif score >=80:   #elif문으로 이동
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'
print(grade)
