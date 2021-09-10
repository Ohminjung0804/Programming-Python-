answer = make_answer()
while True:
    guess = input("뭘까?")
    strike, ball = check(guess, ball)
    print(f'{guess}\tstrike: {strike}, ball: {ball}')
    if answer == guess:
        print("정답입니다.")
        break