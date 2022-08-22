import json
import logging

from firstWeekTask.Exception.input_type_error import NotInMenu
from firstWeekTask.date_time import ConfigDateTime

class Restaurant:
    meal = ['breakfast', 'lunch', 'dinner']
    
    def __init__(self, res_code):
        self.res_code = res_code
        self.menu_list = []
        self.get_json_data()     # 식당 객체가 생기면 해당 객체에 맞는 메뉴가 들어가도록 설정

    def get_json_data(self):
        filepath = './resources/restaurant.json'

        with open(filepath, 'r', encoding="UTF-8") as f:
            json_data = f.read()
            menu = json.loads(json_data)[self.res_code]

            for menu_temp in menu:
                self.menu_list.append(menu[menu_temp])
    
    # 매뉴 보여주는 함수
    def show_menu(self, now_meal):

        if self.menu_list[0] == 'no':
            print("식당 메뉴가 제공되지 않습니다.")
        else:
            print("----------- {} ----------- \t".format(now_meal))
            print('   메뉴               가격')
            for key, value in self.menu_list[1][now_meal].items():
                print(key, '        ', value)
    
    # 메뉴를 선택하는 함수
    def select_menu(self, menu) -> int:
        total = 0
        while True:
            print('메뉴를 입력 || 종료 : 0')
            choice = input()
            if choice == '0':
                break
            try:
                if choice not in self.menu_list[1][ConfigDateTime.now_meal]:
                    raise NotInMenu('메뉴에 없는 음식')
                else:
                    print(self.menu_list[1][ConfigDateTime.now_meal][choice])
                    menu.append(choice)
                    total += int(self.menu_list[1][ConfigDateTime.now_meal][choice])
            except NotInMenu as log:
                logging.exception('NotInMenu : 메뉴에 없는 음식 입력', log)

        return total


# if __name__ == '__main__':
#     user = User('1', 'user')
#     date = ConfigDateTime()
#     ConfigDateTime.now_meal = 'lunch'
#     print(date.now_meal)
#     print(ConfigDateTime.now_meal)
#     res1 = Restaurant('B')
#     res1.show_menu(date.now_meal)
#     # res1.select_menu(user.total, user.menu_list)
#     print(res1.select_menu(user.menu_list))

