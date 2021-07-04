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
'''
seq = int(input())
scr = []
cnt_list = []
for i in range(0,seq): #seq 만큼 반복
    scr.append(list(input()))

for a in scr:
    for x in range(0,len(a)):
        count = 0
        for y in range(x,-1,-1):
            if a[x] == 'O' and a[y] == 'O':
                count += 1
            else:
                break
        cnt_list.append(count)
    print(sum(cnt_list))
    cnt_list.clear()

'''
#4344
case_num = int(input())
for i in range(case_num):
    case = list(map(int,input().split()))
    case.pop(0)
    count = 0
    for x in case:
        if x > sum(case)/len(case):
            count += 1
    percent = count / len(case) * 100
    print('{0:.3f}%' .format(percent))