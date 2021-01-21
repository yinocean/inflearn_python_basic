# Chapter02-1
# 파이썬 완전 기초
# print 사용법
# 참조 :

# 기본 출력
print('python start')
print("python start")
print('''python start''')
print("""python start""")

print()

# separator 옵션(구분자)
print('p', 'y', 't', 'h', 'o', 'n', sep=' ')
print('010', '7777', '1234', sep='-')
print('sokot', 'google.com', sep='@')

print()

# end 옵션
print ('Welcom to', end='  ')
print ('IT News', end='  ')
print('Web Site')

# file 옵션
import sys
print ('Learn Python', file=sys.stdout)
print()

# format 사용(d:3, s:'python', f:3.14123)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))

# %{
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))


print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice'))


print('%.5s' % ('python study'))
print('{:10.5}'.format('python study'))


# %{: value for key, value in variable}
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' %(42))
print('{:4d}'.format(42))


# %f
print('%f' %(3.14123445123))
print('{:f}'.format(3.14123445123))
print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
