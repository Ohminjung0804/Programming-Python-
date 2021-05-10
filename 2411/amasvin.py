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
        return f'이름: {self.name}\t가격: {self.price}\t컵사이즈:{Drink._CUPS[self.cup]}\t얼음량:{Drink._ICES[self.ice]}\t당도:{Drink._SUGARS[self.suger]}'


class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _PEARLS=('타피오카','화이트','알로에','젤리')
    def __init__(self):
        #부모초기화호출
        self.peal=0
    def __str__(self):
        pass


민정이꺼 = Coffee('카페모카',2500)
민정이꺼.order()
print(민정이꺼)