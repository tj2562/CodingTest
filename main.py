#10952
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
while(1):
    a, b = input("a b").split()
    a = int(a)
    b= int(b)
    if (a==0 and b==0):
        break
    print(a + b)
'''
#10951
#EOF
'''
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
'''
'''
N = int(input("N="))
count = 0
newN = N
while(1):
    newN = 10*(newN%10)+(newN//10+newN%10)%10
    count += 1
    if (N == newN):
        break
print(count)
'''
#10818
'''
num = int(input())
a=list(map(int,input().split()))
print(min(a), max(a))
'''
#2562
'''
a= list()
for i in range(1, 10):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)'''
#2577
'''
A = int(input())
B = int(input())
C = int(input())
num = A*B*C
num_list = list(map(int,str(num)))

for i in range(0, 9):
    count = 0
    for j in num_list:
        if i == j:
            count += 1
    print(count)
'''
#3052
'''
a= list()
for i in range(0, 10):
    a.append(int(input())%42)
b = list(set(a))
print(len(b))
'''
#1546
'''
num = int(input())
a = list(map(int,input().split()))
new = [x/max(a)*100 for x in a]
print(sum(new)/len(new))
'''
#8958
seq = int(input())

scr = []
count = 0
for i in range(0,seq): #seq 만큼 반복
    scr.append(list(input()))
print(scr)
for a in scr:
    for x in range(0,len(a)):
        for y in reversed(range(x)):
            if a[y] == a[x]:
                count += 1
            else:
                break

print(count)
'''
for x in range(1,len(scr)+1):
    print(x)
    for j in (x,0):
        print(j)
'''
