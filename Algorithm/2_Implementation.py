#4-1 상하 좌우

'''N = int(input())
plan = list(map(str, input().split()))
x, y = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for i in plan:
    idx = move_types.index(i)
    temp_x = x + dx[idx]
    temp_y = y + dy[idx]
    if temp_x < 1 or temp_x > N or temp_y<1 or temp_y > N:
        continue
    x = temp_x
    y = temp_y

print(x,y)'''

#4-2 시각
#1초의 2000만번 -> 하루는 86400초이므로 충분함 -> 완전탐색문제
'''N = int(input())
time = N * 3600 + 59 * 60 + 59
count = 0
for i in range(time):
    h = int(i/3600)
    m = int((i - 3600 * h)/60)
    s = int(i - 3600*h - 60 * m)
    time =list(map(int, f'{h}{m}{s}'))
    if 3 in time:
        count+=1'''
'''N = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)'''

#4-2 왕실의 나이트

'''dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
col = ['a','b','c','d','e','f','g','h']

inputstr = input()
y,x = inputstr[0], inputstr[1]
x = int(x)
y = col.index(y)
count  = 0
for i in range(8):
    tempx = x + dx[i]
    tempy = y + dy[i]
    if tempx < 1 or tempx > 8 or tempy < 1 or tempy > 8:
        continue
    count += 1
print(count)'''

#4-3 문자열 재정렬
inputstr = input()
alp_list = []
isnum, sum = 0,0
for i in inputstr:
    try:
        i = int(i)
        sum += i
        isnum = 1
    except:
        alp_list.append(i)
alp_list.sort()
if isnum:
    alp_list.append(str(sum))
print("".join(alp_list))