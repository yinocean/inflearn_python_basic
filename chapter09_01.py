#river0123
# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대경로('../, ./'), 절대경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제1

f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)

# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read(): 전체 읽기, read(10) : 10Byte
# read함수 안에 숫자를 int형으로 넣어주면 그 바이트 수만큼 읽어온다

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)

print()

# 에제4
# readline : 1줄씩 읽어ㅇ기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 list로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()

# 파일 쓰기(write)

# 'a' 모드는 append로 기존에 있었던 텍스트에 내용에 추가됨
# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2s\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4
# print문에 보이지않고 파일에 써서 확인
# 콘솔에 print문 내용이 보이지 않을 때 file옵션이 있는지 확인
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
