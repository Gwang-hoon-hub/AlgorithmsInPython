# 메인 서비스
import json
from firstWeekTask.Account.user import User
from firstWeekTask.Exception.input_type_error import NotFoundAccount
from firstWeekTask.date_time import ConfigDateTime
from firstWeekTask.read_file import ReadFile
from firstWeekTask.Restaurant.restaurant import Restaurant
import logging


class MainService:
    date = ConfigDateTime()
    readfile = ReadFile()

    @classmethod
    def app_start(cls):
        print('아이디 입력 : \t')
        account_data = check_id(input())       # 유저 / 매니저 인지 입력받기
        print(account_data)
        if account_data['role'] == 'user':
            make_user = User(account_data['id'], account_data['role'])
            # 식당 입력
            restaurant = input_restaurant()
            # 메뉴 선택 : 현재 시간의 음식 보여주기
            restaurant.show_menu(cls.date.now_meal)
            # restaurant.select_menu(make_user.total, make_user.menu_list)
            make_user.total = restaurant.select_menu(make_user.menu_list)
            # 선택 메뉴 보여주기
            print(make_user.menu_list)
            # 총 금액 보여주기
            print(make_user.total)
        else:
            # 매니저 -> 시간 설정하기
            cls.date.config_time()
            print(cls.date.now_meal)
            cls.app_start()
        pass


def check_id(user_id):
    # ReadFile.class_id = user_id
    with open('./resources/account.json', 'r', encoding='UTF8') as f:
        json_data = f.read()
        account_dict = json.loads(json_data)

        try:
            if user_id not in account_dict:
                raise NotFoundAccount('요청하신 아이디가 없습니다.')
        except NotFoundAccount:
            print('아이디 다시 입력!')
            check_id(input())
    print(account_dict[user_id])
    return account_dict[user_id]


def input_restaurant() -> Restaurant:        # 식당을 선택 한 후 식당 객체를 생성하여 return 한다.
    print('식당을 선택하세요')
    # restaurant = None
    for res in ReadFile.class_res_list:
        print(res, '\t')
    try:
        res_str = input()
        if res_str not in ReadFile.class_res_list:
            raise ValueError
        else:
            restaurant = Restaurant(res_str)

    except ValueError as error_msg:
        logging.exception('식당 선택 오류: ', error_msg)
        restaurant = input_restaurant()

    return restaurant


if __name__ == '__main__':
    MainService.app_start()

# TODO: if __name__ == '__main__': -==? 설명!
