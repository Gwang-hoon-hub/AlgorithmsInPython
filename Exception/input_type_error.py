class TaskException(Exception):
    # def __init__(self, msg):
    #     self.msg = msg
    #
    # def __str__(self):
    #     return self.msg
    pass


class InputTimeError(TaskException):
    # def __init__(self, msg):
    #     super().__init__('입력 시간 오류 이전 식사 시간과 겹침')

    pass

class NotFoundAccount(TaskException):
    # def __init__(self, msg):
    #     super().__init__('등록되어 있지 않은 아이디!')
    pass

        
class NotInMenu(TaskException):
    # def __init__(self, msg):
    #     super().__init__('존재하지 않는 메뉴 입력')
    pass

# todo : 클래스 설계를 다시 할 수 있도록 / 식당이 데이터를 갖고오는데 함수 호출 시 여러번 불러올 수 있지 않도록 진행한다.
# todo :

