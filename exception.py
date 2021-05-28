
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key = lambda x : len(set(list(x))))
print(strings)

a = [1,2,3,4,5]
a.sort(key=lambda x: -x)
print(a)

def squares(n=10):
    print('Generating squares from 1 to {}'.format(n**2))
    for i in range(1, n+1):
        yield i**2
        
gen = squares()
gen	#out: <generator object squares at 0x0000021901407318>
for x in gen:
    print(x, end=' ')
    

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")


try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)