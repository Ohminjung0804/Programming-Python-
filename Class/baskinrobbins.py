class Icecream:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'이름 : {self.name}'

    def set_explanation(self, explanation):
        self.explanation = explanation


아이스홈런볼 = Icecream('아이스홈런볼')
아이스홈런볼.set_explanation('초콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넣이 쏙쏙!')
# print(아이스홈런볼)
# print(아이스홈런볼.explanation)

베리베리스트로베리 = Icecream('베리베리스트로베리')
# print(베리베리스트로베리)

이상한나라의솜사탕 = Icecream('이상한나라의솜사탕')
# print(이상한나라의솜사탕)

민트초콜릿칩 = Icecream('민트초콜릿칩')


# print(민트초콜릿칩)

class Order:
    _CATEGROIES = ('싱글레귤러', '더블레귤러', '파인트')  # 추가가능
    _PRICES = (3200, 6200, 8200)

    def __init__(self):  # 생성자 . 변수 초기화
        self.set_cateries()  # 종류 : 콘, 파인트..
        self.menu = []  # 메뉴
        self.init_menu()
        self.order_menu = []  # 주문한 메뉴

    def __str__(self):
        pass

    def set_cateries(self):
        for index, category in enumerate(Order._CATEGROIES):
            print(index + 1, category)
        category_num = input('종류를 골라주세요:')
        self.category = int(category_num)

    def init_menu(self):
        self.menu.append(Icecream('베리베리스트로베리'))
        self.menu.append(Icecream('이상한나라의솜사탕'))
        self.menu.append(Icecream('민트초콜릿칩'))

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index + 1}.{icecream}')

    def order(self):
        self.show_menu()  # 아이스크림 보여주기(메뉴)
        for _ in range(self.category):  # 종류에 따라 반복 # '_'는 사용하지 않는의미를 가짐
            icecream = input('아이스크림을 골라주세요: ')  # 메뉴선택
            icecream = int(icecream)  # 형변환
            self.order_menu.append(self.menu[icecream - 1])  # 주문한 메뉴에 추가

        # 종류 출력
        print('-' * 10 + '주문 내역 입니다.' + '-' * 10)
        print(Order._CATEGROIES[self.category - 1])
        print(f'{Order._PRICES[self.category - 1]}원')

        # 주문한 메뉴 출력
        for icecream in self.order_menu:
            print(icecream)


order = Order()
order.order()