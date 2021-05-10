class Celebrity:
    def __init__(self,name):
        self.name=name

    def set_name(self,name):
        self.name=name;

    def set_entertainment(self,entertainment):
        self.entertainment=entertainment

    def __str__(self):
        return f'이름 : {self.name}\t소속사 : {self.entertainment}'

class Talent(Celebrity):
    def __init__(self,name):
        super().__init__(name) #Celebrity 클래스의 생성자 호출

    def set_drama(self,drama):
        self.drama=drama

    def __str__(self):
        return super().__str__()+ f'\t드라마: {self.drama}'
        #return f'이름 : {self.name}\t소속사 : {self.entertainment}\t드라마 : {self.drama}'


class Singer(Celebrity):
    def __init__(self,name,song):
        super().__init__(name)
        self.song=song

    def __str__(self):
        return super().__str__()+f'\t노래: {self.song}'

백현 = Celebrity('백현')
#백현.set_name('변백현')
백현.set_entertainment('SM')
#백현.info()
#print(백현.name, 백현.entertainment)
print(백현) #클래스의 __str__()호출됨

이광수=Talent("이광수")
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)

현진=Singer('현진','신메뉴')
현진.set_entertainment('JYP')
필릭스=Singer('필릭스','Back Door')
필릭스.set_entertainment('JYP')
print(현진)
print(필릭스)

스트레이키즈=[]
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(스트레이키즈)
for 멤버 in 스트레이키즈:
    print(멤버)

