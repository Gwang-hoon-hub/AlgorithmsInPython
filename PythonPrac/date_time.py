# 아침, 점심, 저녁 시간을 설정하는 클래스
from datetime import datetime
import time
from firstWeekTask.Exception.input_type_error import InputTimeError

class ConfigDateTime(object):

    breakfastTime = []
    lunchTime = []
    dinnerTime = []
    now = datetime.now()
    now_hour_minute = datetime.strptime(str(now.hour)+':'+str(now.minute), "%H:%M")

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):  # Foo 클래스 객체에 _instance 속성이 없다면
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)  # Foo 클래스의 객체를 생성하고 Foo._instance로 바인딩
        return cls._instance  # Foo._instance를 리턴

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):  # Foo 클래스 객체에 _init 속성이 없다면
            print("__init__ is called\n")
            cls._init = True

    def __str__(self):
        return '아침-점심-저녁 시간을 설정하는 객체'
    #     hour, minute = map(int, time_string.split(':'))

    @classmethod
    def input_date(cls) -> list:
        try:
            input_date_list = input().replace(" ","").split('-')
            print(input_date_list)
            for i in range(len(input_date_list)):
                # 여기 datetime
                input_date_list[i] = datetime.strptime(ConfigDateTime.now.date() + input_date_list[i], '%H:%M')
                # input_date_list[i] = time.strptime(input_date_list[i], '%H:%M')
            if input_date_list[0] > input_date_list[-1]:
                raise InputTimeError

        except InputTimeError as l:
            print(l)

        except Exception as l:
            print('날짜 형태 입력 오류! : ', l)

        else:
            return input_date_list

    @classmethod
    def compare_before_time(cls, str):
        '''
        식사 시간이 이전의 시간과 겹치는지 비교하는 함수
        '''
        if str == '점심':
            if ConfigDateTime.breakfastTime[-1] > ConfigDateTime.lunchTime[0]:
                raise InputTimeError
        if str == '저녁':
            if ConfigDateTime.lunchTime[-1] > ConfigDateTime.dinnerTime[0] or ConfigDateTime.dinnerTime[-1] < ConfigDateTime.breakfastTime[0]:
                raise InputTimeError
        return True

    @classmethod
    def config_time(cls):
        # 아침 시간 설정
        print('아침 시간 설정 : ex) 00:00 - 24:00')
        cls.breakfastTime = cls.input_date()


        print('점심 시간 설정 : ex) 00:00 - 24:00')
        cls.lunchTime = cls.input_date()
        # 이전 시간과 겹치는지 확인하기
        cls.compare_before_time('점심')

        print('저녁 시간 설정 : ex) 00:00 - 24:00')
        cls.dinnerTime = cls.input_date()
        cls.compare_before_time('저녁')

        # print('저녁 시간 설정 : ex) 00:00 - 24:00')
        # input_dinner_time = input().replace(" ", "").split('-')
        # for i in range(len(input_dinner_time)):
        #     input_dinner_time[i] = time.strptime(input_dinner_time[i], '%H:%M')
        # if input_dinner_time[0] < input_dinner_time[-1]:
        #     # raise ValueError
        #     print('입력 오류 에러 발생! --> 식사시간 겹침')
        # if input_dinner_time[0] > input_lunch_time[-1]:
        #     print('입력 시간 오류 --> 시작 시간 끝 시간')


        # ConfigDateTime.dinnerTime = input_dinner_time  # 클래스 변수 아침시간 초기화
        return None



if __name__ == '__main__':
    print('시간 설정 파이썬 : (00:00 - 24:00)')
    print(ConfigDateTime.breakfastTime, ConfigDateTime.lunchTime, ConfigDateTime.dinnerTime)
    inst1 = ConfigDateTime()
    inst1.config_time()
    print('실행 후')
    print(type(ConfigDateTime.breakfastTime[0]))
    print(ConfigDateTime.breakfastTime[0], ConfigDateTime.lunchTime[0], ConfigDateTime.dinnerTime[0])


