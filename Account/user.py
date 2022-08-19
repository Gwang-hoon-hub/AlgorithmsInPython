from firstWeekTask.Account.account import Account


class User(Account):

    # total = 0
    # menu_list = []

    def __init__(self, user_id, role):
        super().__init__(user_id, role)
        self.total = 0
        self.menu_list = []  # 아, 점, 저 메뉴를 선택하면 해당 딕셔너리에 "아침":"메뉴1" -> 행태로 들어가도록 한다.

    def __str__(self):
        return super(User, self).__str__()

    def show_select_menu(self):
        for menu in self.menu_list:
            print(menu)


if __name__ == '__main__':
    user1 = User('user1', 'user')
    print(user1)
    user2 = User('user2', 'user')
    print(user2)
    print(user1 == user2)
