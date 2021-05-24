from recipe import Recipe

class Recipebook:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self):
        # 추가할 레시피 이름 입력받자
        name = input('>> 레시피 이름을 입력하세요: ')

        # 중복 체크하자
        for recipe in self.recipe_list:
            # 중복되는 레시피가 있으면
            if name == recipe.name:
                #중복된다고 알려주자
                print('이미 존재하는 레시피 입니다.')
                return

            # 중복되는 레시피가 없으면
                # 레시피 생성하기
            new_recipe = Recipe(name)
            new_recipe.set_recipe()

            # 레시피리스트에 생성한 레시피 추가하기
            self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index+1}')
            print(recipe)

    def search_recipe(self):    #레시피북에서 레시피 찾기
        #비어있다면 검색한 레시피가 없음
        searched_recipe = []
        #레시피 이름 입력받기(검색)
        name = input('>> 원하는 레시피를 검색하세요: ')
        #리스트에 같은 이름이 있는지 확인하기
        for recipe in self.recipe_list:
            #레시피의 이름이 검색받은 이름과 같은지 확인
            if name == recipe:
                # 같은 이름이 있다면 레시피 출력
                print(recipe)
                searched_recipe.append(recipe)
            #검색된 레시피가 없다면 (searched_recipe가 비어있다면)
            if len(searched_recipe)== 0:
                # 추가할지 물어보자
                answer = int(input('>> 찾는 레시피가 없습니다. 추가하시겠습니까? (1:예 , 0:아니요)'))
                #추가한다고하면
                if answer :
                    # 레시피 추가
                    self.add_recipe()
                else:
                    return








    def __str__(self):
        pass