class Drink:
    _CUPS = ('레귤러','점보') #'레귤러'
    _ICES=('0%','50%','100%','150%')    #'100%'
    _SUGARS=('0%','50%','100%','150%')  #'100%'
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.cup=0 #'레귤러'
        self.ice=2  #100%
        self.suger=2    #'100%'

    def set_cup(self):
        for index,cup in enumerate(Drink._CUPS):     #컵 종류 보여주자 #인덱스와 값을 같이 가져오는 enumerate
            print(f'{index+1}:{cup}')

        cup=input('컵사이즈를 선택하세요: ')      #컵선택
        if cup=='':
            self.cup=2  #enter치면 기본값
        else:
            self.cup=int(cup)-1     #컵 self에 넣기

        if self.cup==1:     #점보면, +500원
            self.price+=500

    def set_ice(self):
        for index,ice in enumerate(Drink._ICES):        #얼음량 종류 보여주기
            print(f'{index-1}:{ice}')

        ice=input('얼음량을 선택하세요: ')       #얼음량 선택
        if ice=='':
            self.ice=2
        else:
            self.ice=int(ice)-1     #얼음량 self에 넣기

        #self.ice=2 if ice=='' else int(ice)-1  #한줄로 작성 가능
    def set_suger(self):
        for index,suger in enumerate(Drink._SUGARS):
            print(f'{index-1}:{suger}')

        suger=input('당도를 선택해주세요: ')
        self.suger=2 if suger=='' else int(suger)-1

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_suger()

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.sugar]}'


class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _PEARLS=('타피오카','화이트','알로에','젤리')
    def __init__(self,name,price):
        super().__init__(name,price)
        #부모초기화호출
        self.peal=0

    def set_pearl(self):
        for index,pearl in enumerate(Drink._PEARLS):
            print(f'{index+1}:{pearl}')

        pearl=input('펄을 선택하세요: ')
        self.pearl=0 if pearl=='' else int(pearl)-1

    def order(self):
        Drink.order()
        self.set_pearl()
    def __str__(self):
        result = super().__str__()
        return result+f'펄종류: {Bubbletea._PEARLS[self.pearl]}'


class Order:
    def __init__(self):
        self.menu = [] #self.menu 매장에 있는 음료수 전체
        self.init_menu()
    def __str__(self):
        s='-'*20+'주문내역'+'-'*20  #주문내역 제목보여주자
        for drink in self.order_menu:
            s+=str(drink) #주문한 음료수 목록 보여주자
        s+=f'총금액: {self.sum_price()}원' #가격 총합계보여주자
        return s
    def init_menu(self):
        사랑이꺼 = Coffee('카페모카',2500)
        하람이꺼 = Bubbletea('오레오 쉐이크',3900)
        에스더꺼 = Bubbletea('타로 밀크티',3300)
        self.menu.append(사랑이꺼)
        self.menu.append(하람이꺼)
        self.menu.append(에스더꺼)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index+1}: {drink}\t{drink.price}원')


    def sum_price(self):
        sum_value=0
        for drink in self.order_drinl.drink:
            sum_value+=drink.price
            return sum_value
    def order_drink(self):
        while True:
            self.show_menu() #메뉴 보여주자
            drink = input('메뉴를 선택하세요: ') #메뉴 선택
            drink= int(drink)-1
            new_drink=self.menu[drink]
            new_drink.order()
            self.order_menu.appdend(new_drink)
            is_add = input("더 주문사시겠습니까?(n :종료)")
            if is_add =='n':
                break
        print(self)


#민정이꺼 = Coffee('카페모카',2500)
#민정이꺼.order()
#print(민정이꺼)
order = Order()