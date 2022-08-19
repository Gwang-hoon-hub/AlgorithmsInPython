from firstWeekTask.Exception.input_type_error import NotFoundAccount
from firstWeekTask.read_file import ReadFile


class AccountRepo:
    user_list = []          # json을 읽은 user 의 데이터 dict 형태로 갖고옴
    user_id_list = []       # account의 id 만 갖고 있는 list

    __intance = None

    def __new__(cls):
        if cls.__intance is None:
            cls.__intance = super(AccountRepo, cls).__new__(cls)
        return AccountRepo.__intance

    def __init__(self):
        self.read_instance = ReadFile()
        AccountRepo.user_list = self.read_instance.account_repo_input_data()

    @staticmethod
    def store_user_id():
        for user_id in AccountRepo.user_list:
            AccountRepo.user_id_list.append(user_id)

    @staticmethod
    def find_user_id(user_id):
        try:
            if user_id not in AccountRepo.user_id_list:
                raise NotFoundAccount('요청한 아이디가 없습니다.')
        except NotFoundAccount:
            print('아이디 다시 입력!')
            AccountRepo.find_user_id(input())
        else:
            return True


if __name__ == '__main__':
    r = ReadFile()
    a = AccountRepo()
    a.store_user_id()
    print(AccountRepo.user_id_list)
