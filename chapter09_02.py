# Chapter09-2
# CSV 파일 읽기 및 쓰기

# CSV : MEME - tet/csv

import csv

# 에제1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)

    # 객체 확인
    print(reader)

    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader)) # __iter__ (for문 사용 가능)
    print()

    for c in reader:
        print(c)
