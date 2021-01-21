# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))
print()

# 동시 선언
x = y = z = 700
print(x,y,z)
print()

# 선언
var = 75

# 재선언
var = "Change value"

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777

n = 777
print(n, type(n))
print()

m = 400
# m -> 777 <- n
print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m)==id(n))
print()


m = 800
n = 800
z = 800
i = 800

print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graaduates

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7

# 예약어는 변수명으로 불가능
class = 2

"""
and	exec	not
assert	finally	or
break	for	pass
class	from	print
continue	global	raise
def	if	return
del	import	try
elif	in	while
else	is	with
except	lambda	yield
"""
print
