#math
import math
print(math.ceil(3.5)) #4 천장, 올림
print(math.floor(3.5)) #3 floor: 바닥, 내림
#반올림
print(round(3.5)) #4
print(round(3.4)) #3
print(math.pow(2, 10)) #1024.0
print(math.sin(math.pi/2)) #1.0

#random
import random
print(random.random())  #java random: 0.0 <= r < 1.0
print(random.randrange(1, 10))  #1 <= r < 10 정수
print(random.randint(1, 10))    #1 <= r <=10 정수
list1 = ['굶었음', '피자', '김치찜', '닭가슴살']
print(random.choice(list1)) #list1 중 하나
print('섞기 전: ', list1)
random.shuffle(list1)     #list1 섞기
print('섞은 후: ', list1)
print(random.sample(list1,2))   #list1에서 랜덤으로 n개 뽑기

#datetime
import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.hour)
birthday = datetime.datetime(2004, 11, 29)
print(birthday)
print(now - birthday)
print('-'*20)

#1
price = 62421
print(round(price,-2))

print(price // 100*100)
print(price - price%100)
print(math.floor(price/100)*100)
print(int(price/100)*100)

print('-'*10)
#2
score =  56
print(round(score,-1), "점")
print(round(score/100)*10)

print('-'*10)
#3
result = []
for i in range(6):
    result .append(random.randint(1,45))
print(result)

print(random.sample(range(1, 45 + 1),6))

print('-'*10)
#4
list2 = [1,2,3,4,5,6,7,8,9]
list3 = []
for i in range(3):
    number = random.choice(list2)
    list3.append(str(number))
    list2.remove(number)
print(list3[0] + list3[1] + list3[2])

list_r = random.sample(range(1,9+1),3)
print("".join(str(n) for n in list_r))  #"".join() - 괄호 안 문자열을 연결
print("".join(map(str, list_r)))
print('-'*10)
#5
import datetime
birth = datetime.datetime(2004, 8, 4)
print(now - birth)

print('-'*10)
#6
from datetime import datetime
christmas = datetime(2021, 12,25)
print(christmas - now)

print('-'*10)
#7
mybirth = datetime(2022,8,4)
print(mybirth - now)

if mybirth < now:
    mybirth = mybirth.replace(year=2022)
    # mybirth.year = mybirth.year + 1

print(mybirth - now)

print('-'*10)
#8
#마지막 번호 묻자
last_number = int(input("마지막 번호는?"))
#1~마지막 번호 까지 숫자 리스트 만들자
list_class = list(range(1, last_number+1))

#반복
while True:
    exclude_number = input("뺄 번호는? (enter치면 그만 빼기)")
    if exclude_number == '':
        break
    list_class.remove(int(exclude_number))

random.shuffle(list_class)
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i+1}\t{number}')