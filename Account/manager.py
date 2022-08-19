from firstWeekTask.Account.account import Account
from firstWeekTask.date_time import ConfigDateTime


class Manager(Account):

    def __init__(self, user_id, role):
        super().__init__(user_id, role)

    def __str__(self):
        return 'Manager Instance!!'

    @staticmethod
    def change_time():
        date_config = ConfigDateTime()
        date_config.config_time()
