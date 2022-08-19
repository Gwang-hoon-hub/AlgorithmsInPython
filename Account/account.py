class Account:
    def __init__(self, user_id, role):
        self.__id = user_id
        self.__role = role
        
    def __str__(self):
        return 'user_id : ', self.__id
