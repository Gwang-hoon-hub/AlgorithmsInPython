import logging

from firstWeekTask.Account.user import User
from firstWeekTask.Restaurant.restaurant import Restaurant
from firstWeekTask.read_file import ReadFile


class RestaurantRepo:  # 실제 레포는 쿼리를 날려주는 곳이다. 데이터를 갖고 있는 곳으로
    res_list = []  # 식당에 대한 모든 데이터

    __intance = None

    def __new__(cls):
        if cls.__intance is None:
            cls.__intance = super(RestaurantRepo, cls).__new__(cls)
        return RestaurantRepo.__intance

    def __init__(self):
        readfile = ReadFile()
        RestaurantRepo.res_list = readfile.store_restaurant()

    @classmethod
    def find_res_name(cls):
        print('식당을 선택하세요')
        for restaurant in cls.res_list:
            print(restaurant)
        try:
            res_str = input()
            if res_str not in cls.res_list:
                raise ValueError
            else:
                restaurant = Restaurant(res_str)

        except ValueError as error_msg:
            logging.exception('식당 선택 오류!! - ', error_msg)
            restaurant = cls.find_res_name()

        return restaurant

    @classmethod  # todo : 다시 설계 다시 설계
    def find_res_menu(cls, restaurant):  # res_code => 생성된 res 코드
        if cls.res_list[restaurant.res_code]['menu_status'] == 'yes':
            for i in cls.res_list[restaurant.res_code]['menu']:
                menu_temp_list = []
                while True:
                    print('메뉴를 입력하면 됩니다  || 종료 : 0')
                    cls.show_menu(i, restaurant)
                    choice = input()
                    if choice == '0':
                        break
                    if choice not in cls.res_list[restaurant.res_code]['menu'][i]:
                        print('잘못 주문!')
                        logging.exception('NotInMenu : 메뉴에 없는 음식 입력')

                    else:
                        print(cls.res_list[restaurant.res_code]['menu'][i][choice])
                        User.total += int(cls.res_list[restaurant.res_code]['menu'][i][choice])
                        menu_temp_list.append(choice)
                    User.menu_list.append(menu_temp_list)
        else:
            print('메뉴를 보여주지 않는 식당')

    @classmethod
    def show_menu(cls, i, restaurant):
        print("----------- {} ----------- \t".format(i))
        print('   메뉴               가격')
        for k, v in cls.res_list[restaurant.res_code]['menu'][i].items():
            print(k, '        ', v)



if __name__ == '__main__':
    r1 = RestaurantRepo()
    print('식당 레포 : ', r1.res_list)

    res = r1.find_res_name()
    print('식당코드 : ', res.res_code)

    r1.find_res_menu(res)
