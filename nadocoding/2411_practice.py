#
# #자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
#
# #문자열 자료형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)
#
# #boolean 자료형
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not(5>10))
#
# #변수
# #애완동물을 소개해 주세요~
# animal="고양이"
# name="해피"
# age=4
# hobby="낮잠"
# is_adult=age>=3
#
# '''이렇게
# 하면 여러문장이 주석처리 됩니다'''
#
# print("우리집" +animal+" 의 이름은" +name+ " 예요")
# hobby="공놀이"
# #print(name+" 는 " +str(age)+ "살이며, "+hobby+ "을 아주 좋아해요")
# print(name+"는 " ,age, "살이며, ",hobby, "을 아주 좋아해요")
# print(name+ " 는 어른일까요? "+str(is_adult))
#
#
# #Quiz) 변수를 이용하여 다음 문장을 출력하시오
#
# #변수명 : station
# #변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# #출력문장 : xx행 열차가 들어오고 있습니다.
# station="사당"
# print(station+"행 열차가 들어오고 있습니다.")
# station="신도림"
# print(station+"행 열차가 들어오고 있습니다.")
# station="인천공항"
# print(station+"행 열차가 들어오고 있습니다.")
#
#
# #연산자
# print(1+1) #2
# print(3-2) #1
# print(5*2) #10
# print(6/3) #2
#
# print(2**3) #2^3=8
# print(5%3) #2
# print(10%3) #1
# print(5//3) #1
# print(10//3) #3
#
# print(10>3) #True
# print(4>=7) #False
# print(10 <3) #False
# print(5<=5) #True
#
# print(3 ==3) #True
# print(4 ==2) #False
# print(3+4 ==7) #True
#
# print(1 !=3) #True
# print(not(1 !=3)) #False
#
# print((3 > 0) and (3 < 5)) #True
# print((3 > 0) & (3 < 5)) #True
#
# print((3>0) or (3>5)) #True
# print((3>0) | (3>5)) #True
#
# print(5> 4 >3) #True
# print(5>4>7) #False
#
# #간단한 수식
# print(2+3*4) #14
# print((2+3)*4) #20
# number = 2+3*4 #14
# print(number)
# number = number+2 #16
# print(number) #16
# number +=2 #18
# print(number) #18
# number *=2 #36
# print(number)
# number /=2 #18
# print(number)
# number -=2 #16
# print(number)
#
# number %=5 #1
# print(number)
#
# #숫자 처리 함수
# print(abs(-5)) #5
# print(pow(4, 2)) #4^2 = 4*4=16
# print(max(5, 12)) #12
# print(min(5,12)) #5
# print(round(3.14)) #3
# print(round(4.99)) #5
#
# from math import *
# print(floor(4.99)) #내림, 4
# print(ceil(3.14)) #올림, 4
# print(sqrt(16)) #제곱근, 4
#
# #댄덤 함수
# from random import *
# # print(random()) #0.0 ~ 1.0미만의 임의의 값 생성
# # print(random()*10) #0.0~10.0미만의 임의의 값 생성
# # print(int(random())*10) #0~10미만의 임의의 값 생성
# # print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# # print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# # print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# # print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# # print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
#
# # print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# # print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# # print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# # print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# # print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# # print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
#
#
# print(randrange(1,45)) #1~46미만의 임의의 값 생성
# print(randrange(1,45)) #1~46미만의 임의의 값 생성
# print(randrange(1,45)) #1~46미만의 임의의 값 생성
# print(randrange(1,45)) #1~46미만의 임의의 값 생성
# print(randrange(1,45)) #1~46미만의 임의의 값 생성
# print(randrange(1,45)) #1~46미만의 임의의 값 생성
#
# print(randint(1,45)) #1부터 45 이하의 임의의 값 생성
# print(randint(1,45)) #1부터 45 이하의 임의의 값 생성
# print(randint(1,45)) #1부터 45 이하의 임의의 값 생성
# print(randint(1,45)) #1부터 45 이하의 임의의 값 생성
# print(randint(1,45)) #1부터 45 이하의 임의의 값 생성
# print(randint(1,45)) #1부터 45 이하의 임의의 값 생성
#
# #Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# #월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# #아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
#
# #조건1: 랜덤으로 날짜를 뽑아야 함
# #조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
# #조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외
#
# date=randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월"+str(date)+"일로 선정되었습니다.")
#
#
# #문자열
# sentence="나는 소년입니다."
# print(sentence)
# sentence2='파이썬은 쉬워요'
# print(sentence2)
# sentence3="""나는 소년이고,
# 파이썬은 쉬워요"""
# print(sentence3)
#
#
# #슬라이싱
# jumin = "990120-1234567"
# print("성별: "+jumin[7])
# print("연: "+jumin[0:2]) #0부터 2 직전까지 (0,1)
# print("월: "+jumin[2:4])
# print("일: "+jumin[4:6])
#
# print("생년월일: "+jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리: "+jumin[7:]) #7부터 끝까지
# print("뒤 7자리 (뒤에서부터) : "+jumin[-7:]) #맨뒤에서 7번쨰부터 끝까지
#
#
# #문자열 처리함수
# python="Python is Amazing"
# print(python.lower()) #모두 소문자로
# print(python.upper()) #모두 대문자로
# print(python[0].isupper()) #인덱스값이 대문자면 True, 소문자면 False
# print(len(python)) #문자열의 길이
# print(python.replace("python","Java")) #문자열 부분을 다른 문자로 바꾸기
#
# index= python.index("n") #찾을 문자열을 넣으면 인덱스값 반환
# print(index)
# index = python.index("n",index+1) #두번째 n 찾기
# print(python)
#
# print(python.find("n")) #n의 위치를 인덱스로 반환, 없다면 -1반환
# #print(python.index("Java")) #index는 오류뜸
# print(python.count("n")) #n이 나온 횟수 반환
#
#
# #문자열 포멧
# #print("a" + "b")
# #print("a","b")
# #방법1
# # print("나는 %d살입니다." %20)
# # print("나는 %s을 좋아해요." %"파이썬")
# # print("Apple은 %c로 시작해요." %"A")
# # print("나는 %d살입니다." %20)
# # print("나는 %s색과 %s색을 좋아해요." %("파란 ","빨간"))
# #
# #
# # #방법2
# # print("나는 {}살입니다.".format(20))
# # print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# # print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
# # print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))
# #
# #
# #방법3
# # print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간색"))
# #
# #방법4
# age=20
# color="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")
#
#
# #탈출문자
# print("백문이 불여일견 \n 백견이 불여일타")
# #\n : 줄바꿈
# #\' \" : 문장 내에서 따옴표
# print('저는 "나도코딩"입니다.') #작은 따옴표 적기
# print("저는 \"나도코딩\"입니다.")
#
# #\\ : 문장 내에서는 \
# #\r : 커서를 맨 앞으로 이동
# print("Red Apple\rpine")
#
# #\b : 백스페이스( 앞에 한 글자 삭제)
# print("Redd\bApple")
#
# #\t : 탭
# print("Red\tApple")
#
#
#
# #Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# #예) http://naver.com
# #규칙1:http:// 부분은 제외 =>naver.com
# #규칙2:처음 만나는 점 이후 부분은 제외
# #규칙3:남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e'갯수 +"!"로 구성
# #                  (nav)       (5)        (1)         (1)
# #예) 생성된 비밀번호 : nav51!
#
# site="http://naver.com"
# first_cut=site[7:10]
# count=len(site[8:13])
# e_number=site.count("e")
# print("생성된 비밀번호: "+ first_cut+str(count)+str(e_number)+"!")
#
#
# #리스트 : 순서를 가지는 객체의 집합
#
# #지하철 칸별로 10명, 20명, 30명
# subway=[10,20,30] # 순서대로 들어감
# print(subway)
#
# subway=["유재석","조세호","박명수"]
# print(subway)
#
# #조세호씨가 몇 번째 칸에 타고있는가
# print(subway.index("조세호"))
#
# #하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") #요소 추가
# print(subway)
#
# #정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1,"정형돈") #정형돈은 인덱스 1번을 넣는다
# print(subway)
#
# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #맨뒤 요소를 없앰
# print(subway)
#
# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")) #같은 값의 갯수
#
# #정렬도 가능
# num_list=[5,2,4,3,1]
# num_list.sort() #작은 순서로 정렬
# print(subway)
#
# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)
#
# #모두 지우기
# num_list.clear()
# print(num_list)
#
# #다양한 자료형 함께 사용
# mix_list=["조세호" ,20, True]
# print(mix_list)
#
# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)
#
#
# #사전
# cabinet={3:"유재석",100:"김태호"}
# # print(cabinet[3]) #key값 넣기
# # print(cabinet[100])
# #
# # print(cabinet.get(3))
# # print(cabinet[5]) #key값이 없으면 프로그램 종료
# # print(cabinet.get(5)) #key값이 없으면 None반환
# # print(cabinet.get(5,"사용가능")) #key값 없으면 뒤에 문자열 출력
#
# # print(3 in cabinet) #3이라는 key가 cabinet에 있다면 True, 없다면 False
# #
# # cabinet={"A-3":"유재석","B-100":"김태호"}
# # print(cabinet["A-3"])#문자도 가능
#
# #새손님
# # cabinet["A-3"]="김종국"
# # cabinet["c-20"]= "조세호" #새로 추가, 이미 key값이 있다면 새로 값을 업데이트
# # print(cabinet)
# #
# # #간 손님
# # del cabinet["A-3"] #A-3key 삭제
# #
# # #key들만 출력
# # print(cabinet.keys())
# #
# # #value들만 출력
# # print(cabinet.values())
# #
# # #key,value 쌍으로 출력
# # print(cabinet.items())
# #
# # #목욕탕이 폐점
# # cabinet.clear() #모든 값 삭제
# # print(cabinet)
#
# #튜플 (리스트보다 빠름)
# # menu=("돈까스","치즈까스")
# # print(menu[0])
# # print(menu[1])
# # # 튜플은 값을 추가하거나 변경할 수 없음
# #
# # name="김종국"
# # age=20
# # hobby="코딩"
# # print(name,age,hobby)
# #
# # (name, age, hobby)=("김종국",20,"코딩")
# # print(name,age,hobby)
#
# #집합(set)
# #중복안됨, 순서없음
# my_set={1,2,3,3,3}
# print(my_set)
#
# java={"유재석","김태호","양세형"}
# python=set(["유재석","박명수"])
#
# #교집합 (java와 python을 모두 할 수 있는 사람)
# print(java & python) #공통되는 값 출력
# print(java.intersection(python))
#
# #합집합 (java도 할 수 있거나 python할 수 있는 개발자)
# print(java | python)
# print(java.union(python))
#
# #차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java-python)
# print(java.difference(python))
#
# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
#
# #java를 잊어버림
# java.remove("김태호")
# print(java)
#
#
# #자료구조의 변경
# menu={"커피",'우유',"주스"}
# print(menu,type(menu))
#
# menu=list(menu)
# print(menu, type(menu))
#
# menu=tuple(menu)
# print(menu,type(menu))
#
# menu=set(menu)
# print(menu,type(menu))
#
#
#
# #Quiz)당신의 학교에서는 파이썬 코딩 대회를 주푀합니다.
# #참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# #댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# #추첨 프로그램을 작성하시오
#
# #조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# #조건2: 댓글 내용과 상과 없이 무작위로 추첨하되 중복 불가
# #조건3: random모듈의 shuffle 과 sample을 활용
# #shuffle- 리스트안을 무작위로 순서 바꿈
# #sample(변수, 1)- 변수리스트 안에서 한개의 값을 램덤으로 출력
#
# from random import *
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(list)
#
# winners=sample(list,4)
#
# print("--당첨자 발표--")
# print("치킨 당첨자: {0}".format(winners[0]))
# print("커피 당첨자: {0}".format(winners[1:]))
#
#
# #if
# weather = input("오늘 날씨는 어때요?")
# if weather=="비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("준비물 필요 없어요.")

# #for문
# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")
#
# for waiting_no in range(1,6): #1,2,3,4,5까지
#     print("대기번호 : {0}".format(waiting_no))
#
# starbucks = ["아이언맨","토르","아이엠","그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# #while
# customer = "토르"
# index =5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index-=1
#     if index ==0:
#         print("커피는 폐기처분 되었습니다.")
#
# customer = "아이언맨"
# index =1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer,index))
#     index +=1

#
# customer ="토르"
# person="Unknown"
# while person !=customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person=input("이름이 어떻게 되세요?")

#continue와 break
# absent=[2,5] #결석
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐.".format(student))
#
#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함
# student = [1,2,3,4,5]
# print(student)
# student=[i+100 for i in student] #students에서의 값을 i에 불러오고 i에 100을 더함
# print(student)

#학생 이름을 길이로 변환
# student=["Iron man","Thor","I am groot"]
# student=[len(i) for i in student]
# print(student)

#학생 이름을 대문자로 변환
# student=["Iron man","Thor","I am groot"]
# student=[i.upper() for i in student]
# print(student)


#Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님 입니다.
#50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성

#조건1 : 승객별 운행 소요 시간은 5분 ~10분 사이의 난수로 정해짐
#조건2 : 당신은 소요 시간 5분 ~15분 사이의 승객만 매칭해야 합니다.

#출력문 예제
#[0] 1번째 손님 (소요시간: 15분)
#[] 2번째 손님 (소요시간 : 50분)
#...
#[]50번째 손님 (소요시간 : 16분)
#총 탑승 승객 2분
#
# from random import *
# cnt =0 #총 탑승 승객 수
# for i in range(1, 51): #1~50이라는 수(승객)
#     time=randrange(5,51) #5분 ~50분 소요 시간
#     if 5 <= time <=15: #5~15이내의 승객, 탑승 승객 수 증가 처리
#         print("[0] {0}번째 손님 (소요시간: {1}분)".format(i,time))
#         cnt +=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i,time))
#
# print("총 탑승 승객: {0}분".format(cnt))

#함수
#어떤 역할을 하는 박스
#
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# open_account()

#전달값과 반환값
# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
#     return balance+money
#
# def withfraw(balance,money): #출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance-money
#     else:
#         print("잔액부족 잔액은 {0}원입니다.".format(balance))
#         return balance
#
# def withdraw_night(balance,money):
#     commission =100 #수수료
#     return commission, balance-money-commission
#
# balance=0
# balance = deposit(balance,1000)
# balance=withfraw(100000,500)
# commission, balance=withdraw_night(balance, 500)
# print("수수료는 {0}원 이며, 잔액은 {1}원입니다.".format(commission,balance))

#기본값
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주사용언어: {2}".format(name,age,main_lang))
#
# profile("유재석", 20,"파이썬")
# profile("김태호", 25,"자바")

#같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이: {1}\t주사용언어: {2}".format(name,age,main_lang))
#
# profile("유재석")
# profile("김태호")

#키워드 값
# def profile(name, age, main_lang):
#     print(name,age,main_lang)
#
# profile(name="유재석",main_lang="파이썬",age=20)
# #순서가 뒤섞여 있어도 가능
#
# #가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}".format(name, age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)
#
# profile("유재석",20,"PYthon","java","C","C++","C#")
# print("김태호",25,"Kotlin","Swift", "","","")

# def profile(name, age, *language): #*은 서로 다른 갯수의 값을 넣을 떄 사용
#     print("이름: {0}\t나이: {1}".format(name, age),end=" ")
#     for lang in language:
#          print(lang, end=" ")
#     print()
#
# profile("유재석",20,"PYthon","java","C","C++","C#","javaScript")
# profile("김태호",25,"Kotlin","Swift")

#지역변수와 전역변수
#지역변수: 함수내에서만 사용가능
#전역변수: 프로그램내에서 어디서나 사용가능

# gun=10
# def checkpoint(soldiers): #경계근무
#     global gun #전역 공간에 있는 gun 사용 golbal : 함수내에서 함수밖에 있는 변수 사용
#     gun= gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# gun = checkpoint_ret(gun,2)
# print("남은 총: {0}".format(gun))



#Quiz ) 표준 체중을 구하는 프로그램을 작성하시오
#*표준 체중 : 각 개인의 키에 적당한 체중

#성별에 따른 공식
#남자: 키(m) X 키(m) X 22
#여자: 키(m) X 키(m) X 21

#조건1 : 표준 체중은 별도의 함수 내에서 계산
#       *함수명 : std_weight
#       *전달값 : 키(height), 성별(gender)
#조건2 : 표준 체중은 소수점 둘째자리까지 표시

#출력예제 : "키 175cm 나자의 표준 체중은 67.38kg 입니다."

# def std_weight(height, gender):
#     if gender=="남자":
#         result =round(height*height*22,2)
#         return print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height,result))
#     elif gender == "여자":
#         result = round(height*height* 21,2)
#         return print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height,result))
#
# height=175
# gender="여자"
# std_weight(height/100, "여자")


#마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name="마린" #유닛의 이름
# hp=40 #유닛의 체력
# damage =5 #유닛의 공격력
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp,damage))
#
# #탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp=150
# tank_damage=35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp,tank_damage))
#
# tank2_name = "탱크2"
# tank2_hp=150
# tank2_damage=35
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력{1}\n".format(tank2_hp,tank2_damage))
#
# def attack(name,location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(name,location,damage))
#
# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# attack(tank2_name,"1시",tank2_damage)

# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력{0}, 공격력{1}".format(self.hp,self.damage))
#
# # marine1 = Unit("마린",40,5)
# # marine2 = Unit("마린",40,5)
# # tank = Unit("탱크",150,35)
#
# #레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1=Unit("레이스",80,5)
# print("유닛 이름 : {0},공격력 : {1}".format(wraith1.name,wraith1.damage))
#
# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(뺴앗음)
# wraith2=Unit("레이스",80,5)
# wraith2.clocking=True

# if wraith2.clocking==True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#
# class AttackUnit:
#     def __init__(self,name,hp,speed:
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         self.speed = speed
#
#     def attack(self,location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}".format(self.naem,location,self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} dlqslek. ".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)
#from random import*
# class Unit:
#      def __init__(self,name,hp,speed):
#          self.name=name
#          self.hp=hp
#          self.speed=speed
#          print("{0} 유닛이 생성되었습니다.".format(self.name))
#          print("체력{0}, 공격력{1}".format(self.hp,self.damage))
#
# # marine1 = Unit("마린",40,5)
# # marine2 = Unit("마린",40,5)
# # tank = Unit("탱크",150,35)
#
# #레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 =Unit("레이스", 80,5)
# print("유닛 이름: {0}, 공격력 : {1}" .format(wraith1.name, wraith1.damage))
# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("레이스",80,5)
# wraith2.clocking = True;
#
# if wraith2.clcking == True:
#     print("{0}는 현재 클로킹 상태입니다. ".format(wraith2.name))
#
# class AttackUnit(Unit):
#     def __init__(self, name, hp,damage):
#         Unit.__init__(self,name,hp)
#         self.damage=damage
#
#     def attack(self,location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(self.name,location,self.damage))
#
#     def damaged(self,damage):
#         print("{0}: {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0 :
#             print("{0} :파괴되었습니다.".format(self.name))
#

# class Marine(SttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self,"마린",40,1,5)
#
#     def stimpack(self):
#         if self.hp >10:
#             self.hp -=10
#             print("{0} : 스팀팩을 사용하빈다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
#
#
# class Tank(AttackUnit):
#     seize_developed = False
#
#     def __init__(self):
#         AttackUnit.__init(self,"탱크",150,1,35)
#         self.seize_mode=False
#
#     def set_size_mod(self):
#         if Tank.seize_developed ==False:
#             return
#
#         if self.seize_mode==False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *=2
#             self.seize_mode=True
#         else:
#             print("{0} : 시즈모드를 해제제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False
#v파이어뱃 : 공격 유닛, 화염방사기
# firebat1= AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
#
# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)
#
#
# #드랍쉽 : 공중 유닛, 수송기, 마린 /파이어뱃/탱크 등을 수송. 공격 x
# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}".format(name,location,self.flying_speed))
#
# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self,name,hp,damage,flying_speed):
#         AttackUnit.__init__(self,name,hp,0,damage) #지상스피드는 0
#         Flyable.__init__(self,flying_speed)
#     def move(self,location):
#         print("공중 유닛 이동")
#         self.fly(self.name,location)
#
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,"레이스",80,20,5)
#         self.clocked =False
#
#     def clocking(self):
#         if self.clocked ==True:
#             print("{0} :클로킹 모드 해제합니다.".format(self.name))
#             self.clocked=False
#         else:
#             print("{0} :클로킹 모드 설정합니다.".format(self.name))
#             self.clocked =True

# #발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

#벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐",80,10,20)

#배틀크루저 : 공중유닛, 체력도 괸장히 좋음, 공격력도 좋음
# battlecruiser=FlyableAttackUnit("배틀크루저",500,25,3)

# vulture.mave("11시")
# battlecruiser.move(battlecruiser.name,"9시")
#
# 건물
# class BuidingUnit(Unit):
#     def __init__(self,name,hp,location):
#         super().__init__(name,hp,0)
#         self.location = location
#
# 서플라이 디폿 : 건물, 1개 건물 = 8유닛
# supply_depot = BuidingUnit("서플라이 디폿",500,"7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     print("player : gg")
#     print("[Player]님이 게임에서 퇴장하셨습니다.")
#
# game_start()
# m1=Marine()
# m2=Marine()
# m3=Marine()
#
# t1=Tank()
# t2=Tank()
#
# w1=Wraith()
#
# attack_units=[]
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)
#
# for unit in attack_units:
#     unit.move("1시")
#
# Tank.seize_developed =True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
#
# for unit in attack_units:
#     if isinstance(unit,Marine):
#         unit.stimpack()
#     elif isinstance(unit,Tank):
#         unit.set_size_mod()
#     elif isinstance(unit,Wraith):
#         unit.clocking()
#
# for unit in attack_units:
#     unit.attack("1시")
#
# for unit in attack_units:
#     unit.damaged(random(5,21))
# game_over()
#
# class Unit:
#     def__init__(self):
#         print("Unit 생성자")
#
#
# class Flyable:
#     def__init__(self):
#     print("Flyable 생성자")
#
#
# class UFlyableUnit(Unit,Flyable):
#     def__init__(self):
#         super().__init__()
#         Unit.__init__(self)
#         Flyable.__init__(self)
#
#
# 드랍쉽
# dropship = FlyableUnit()
#
#
#
#Quiz ) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

#(출력예제)
#총 3대의 매물이 있습니다.
#강남 아파트 매매 10억 2010년
#마포 오피스텔 전세 5억 2007년
#송파 빌라 월세 500/50 2000년
# class House:
#     def __init__(self,location,house_type,deal_type,price,competion_year):
#         self.location=location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price=price
#         self.completion_year=competion_year
#
#     def show_detail(self):
#         print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)
#
# houses=[]
# house1 = House("강남","아파트","매매","10억","2010년")
# house2 = House("마포","오피스텔","전세","5억","2007년")
# house3 = House("송파","빌라","월세","500/50","2000년")
#
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
#
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()



