# 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv
import csv

with open('../resource/sample1.csv', 'r') as f:
    reader = csv.reader(f) # 구분자가 기본적으로 ,(콤마)를 갖는다.
    # 갖고 온 데이터를 출력하면 맨 위의 row를 갖고온다. --> ['번호', '이름', '가입일시', '나이']
    # 이를 넘어가기 위해서 next() 함수를 사용한다.
    next(reader) # Header를 스킵

    #확인
    print(reader) # ==>   <_csv.reader object at 0x000001A30954F8D0>
    print(type(reader))  # <class '_csv.reader'>
    print(dir(reader))   # ==> dir로 어떤 함수를 갖고 있는지 확인한다. __iter__ 함수를 갖고 있으면 반복문을 돌릴 수 있다.

    for r in reader:
        #print(type(r)) # <class 'list'>
        print(r) # ==> 하나의 row를 list로 갖고와서 보여준다.

# 구분자 활용
with open('../resource/sample2.csv', 'r') as f:
    #reader = csv.reader(f)
    reader = csv.reader(f, delimiter='|') # delimiter='|' 는  '|'로 구분을 하여 값을 갖고온다.

    for r in reader:
        print(r) # ['1|김정수|2017-01-19 11:30:00|25'] 구분을 하지 않는다.

#Dict 변환
with open('../resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # Header row의 값을 dictionary의 key 값으로 하여 데이터를 딕셔너리 형태로 보여준다.

    # for r in reader:
    #     print(r)

    for r in reader:
        for k, v in r.items():
            print(k,v)
        print('-----------')

# csv 파일 사용
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
with open('../resource/custom2.csv', 'w', newline='') as f: # newline ==> 새로운 줄바꿈에 대한 처리를 어떻게 할 것인가?
    # # newline 줄바꿈 처리한 코드는 custom2.csv 이다.
    wt = csv.writer(f)

    for v in w:
        # 하나하나 검수를 해서 적고자 한다면 writerow를 사용한다.
        wt.writerow(v)

# for문 없이 한번에 write 하기
with open('../resource/custom3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)
    # 검수 없이 모두 적고자 한다면 writerows를 사용한다.


# 엑셀 읽기 XSL, XLSX
# 엑셀을 여는 것을 이용하여 pandas를 주로 사용 : openpyxl, xlrd
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

xlsx = pd.read_excel('../resource/sample.xlsx')