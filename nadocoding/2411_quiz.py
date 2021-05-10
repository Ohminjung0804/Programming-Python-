# 1-1
# 주민등록번호 앞 6자리를 변수 id_number에 넣고, 출생년도 끝 두자리 \n출생 월일 \n 그 두개의 합 출력
# id_number="020316"
# year=(int)(id_number[:2])
# month_day=(int)(id_number[2:])
# print(id_number[:2]+"\n"+id_number[2:]+"\n"+str(month_day+year))
# print("\n")
#
# #1-2
# #집 전화번호를 phone_number에 넣고,
# #지역번호\n 맨 끝 네자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# phone_number="02-1234-5678".split('-')
# print("지역번호: "+phone_number[0]+"\n"+"끝 네자리: "+phone_number[2])

# 휴대폰 번호를 입력할 때 -있든, 없든, 없이 출력하기
# phone_number1='010-2540-5357'
# phone_number2='010 7584 1367'
# phone_number3='01073201685'
# phone_number=phone_number1
#
# result=phone_number.replace('-','').replace(' ','')
# print(result)
#


# 2-1
# 학번을 student_number변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0미만이거나 7이상이면 "잘못입력했습니다."출력하기
# student_number ='2100' 또는 '2000'
# <출력예시>   1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
# student_number='2411'
# number=student_number[1]
# number=int(number)
# majors=["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"]
# if 1<=number<=6:
#     print(f"{number}반 {majors[(number -1)//2]}")
# else:
#     print("잘못입력했습니다.")


# 2-2
# 학번을 함수인 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# 함수호출
# grade, major = get_major("2100")
# print(major,grade) #뉴미디어소프트웨어과2
# def get_major(argumenet):
#     if argumenet[1]=="1" or argumenet[1]=="2":
#         major="뉴미디어소프트웨어과"
#         return argumenet[0],major
#     elif argumenet[1]=="3" or argumenet[1]=="4":
#         major="뉴미디어웹솔루션과"
#         return argumenet[0],major
#     elif argumenet[1]=="5" or argumenet[1]=="6":
#         major="뉴미디어디자인과"
#         return argumenet[0],major
#
# grade,major=get_major("2411")
# print(major,grade)

# def get_major(student_number):
#     majors=['소','소','솔','솔','디','디']
#     grade=student_number[0]
#     classroom=student_number[1]
#     return grade,majors[classroom-1]
#
# grade, major=get_major('2100')
# print(major,grade)


# 2-3
# 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면
# 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수호출>
# print(average(10,20,30)) #20.0
# print(average(4,23)) #13.5

# def average(*number):
#     sum=0
#     for i in number:
#         sum+=i
#     return(sum/len(number))
#
# print(average(10,20,30,40,50))


# 2-4
# 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)

# *BMI지수 계산법 : 체중(kg) / 키의 제곱
# 18.5 미만 : 저체중
# 18.5이상 23 미만 : 보통
# 23 이상 25 미만 : 과체중
# 25이상 : 비만

# <함수호출>
# bmi = get_bmi(176,69)
# print(bmi) #22.3

# def get_bmi(height, weight):
#     height/=100
#     bmi=round((weight/(height*height)),1)
#     if bmi>18.5:
#         return "저체중"
#     elif 18.5<=bmi<23:
#         return "보통"
#     elif 23<=bmi<25:
#         return "과체중"
#     elif bmi >25:
#         return "비만"
#
# bmi=get_bmi(176,69)
# print(bmi)

# def get_bmi(height,weight):
#     height/=100
#     bmi=weight/height**2
#     return bmi
#
#
# bmi=get_bmi(176,69)
# print(bmi)


# for i in range(2,10):
#     for j in range(1,10,2):
#         print(f'{i}X{j}={i*j}')
#     print()
#     if i ==7:
#         break


# Quiz3-1
# n_sum()함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다
# 작은 숫자를 넣으면, 각자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
# def n_sum(argument) :
#     if argument<1000000000 :
#         new = str(argument)
#         sum = 0
#         # for i in range(len(new)):
#         #     sum += int(new[i])
#         for i in new :      # i: '4' '0' '8'
#             sum+=int(i)
#         return sum
#     else:
#         return -1
#
#
#
# result = n_sum(10)
# print(result)  # 1
# result = n_sum(331)
# print(result)  # 7
# result = n_sum(408)
# print(result)  # 12
# result = n_sum(1000000000)
# print(result)  # -1
# print()
#
#
# # Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면,
# # 요금을 리턴한다. * 지하철 요금계산법 10km 이내: 720원(청소년),
# # 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
# def get_subway_fare(km):
#     if km<=10:
#         return 720
#     elif 10<km<=50: #26
#         cnt=0
#         for i in range(15,51,5):        # i: 15 20, 25, 30, 35, 40, 45, 50
#             if i<=km:
#                 cnt+=1
#             elif i>km:
#                 if km+5-i >0 :
#                     cnt+=1
#                 break
#         return 720+(cnt*100)
#     elif km>50:#61
#         cnt=0
#         sum_km=58
#         while True:
#             if km>sum_km:
#                 sum_km+=8
#                 cnt+=1
#             else:
#                 break
#         return 1620+(cnt*100)
#
#
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(25)
# print(fare)        #1020
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720
# fare = get_subway_fare(67)
# print(fare)        #1720
# print()
#
# # Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# # * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# def get_three_six_nine(number):
#     cnt = 0
#     number = str(number)
#     for i in range(3, 10, 3):       #3 6 9
#         i = str(i)
#         cnt += number.count(i)
#
#     if cnt == 0:
#         return number
#     else:
#         return "짝" * cnt
#
#
# result = get_three_six_nine(1)
# print(result)  # 1
# result = get_three_six_nine(3)
# print(result)  # 짝
# result = get_three_six_nine(16)
# print(result)  # 짝
# result = get_three_six_nine(36)
# print(result)  # 짝짝
#
#
# #prime()함수를 만든다. 이함수에 매개변수(number)를 입력하면 입력받은 수가 소수인지 판별하는
# #프로그램을 작성.
# #
# def prime(number):
#     if number !=1:
#         for i in range(2,number):
#             if number %i ==0:
#                 return "소수가 아님"
#     else:
#         return "소수가 아님"
#     return "소수"
#
# result=prime(7)
# print(result)  #소수
# result=prime(25)
# print(result)  #소수가 아님


#
# Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.

# def is_prime(prime_number):
#     if prime_number != 1:
#         for i in range(2,prime_number):
#             if prime_number %i ==0:
#                 return "소수 아님"
#             else:
#                 return "소수 아님"
#     return "소수"
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님





#Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
# def is_prime(prime_number):
#     if prime_number==1:
#         return "소수아님"
#     for i in range(2,prime_number):
#         if prime_number%i==0:
#             return "소수아님"
#         else:
#             return "소수"
#     return "소수"
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님



'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
'''
def get_compliment(answer):
    if '고구마' in answer:
        return "왓쇼이!"
    elif '맛있는' in answer:
        return "우마이!"
    elif '놀랄 만한' in answer:
        return "요모야..!"
    elif '황당한' in answer:
        return "요모야..!"
    elif '굉장한' in answer:
        return "요모야..!"
    else:
        return "으무!"




result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!
