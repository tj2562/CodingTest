'''
n = int(input())
count = 0
mem = list(map(int, input().split()))
mem.sort(reverse= True)
while len(mem) >= 1 and len(mem) >= mem[0]:
    for i in range(mem[0]):
        mem.pop(0)
    count += 1
print(count)'''
#2
'''S = list(map(int, input()))
result = S[0]
for i in S[1:]:
    result = max(result*i, result+i)
print(result)'''
#3
'''import math
s = list(map(int, input()))
count = 0
for i in range(len(s)-1):
    if s[i+1] != s[i]:
        count += 1
print(math.ceil(count/2))'''
#4
'''n = int(input())
coin = list(map(int, input().split()))
coin.sort()
target = 1
for i in coin:
    if target < i:
        break
    target += i

print(target)'''

#5
'''n, m = map(int, input().split())
num = list(map(int, input().split()))
count = 0
for i in range(len(num)):
    for j in num[i+1:]:
        if num[j] == num[i]:
            count += 1

print( n*(n-1)/2 - count)'''

#6
'''def solution(food_times, k):
    n = len(food_times)
    index = 0
    answer = 0
    count = 0
    while count < k:
        if food_times[index % n] > 0:
           food_times[index % n] -= 1
           count += 1
        if sum(food_times) == 0:
            return -1
        index += 1

    while True:
        if food_times[index%n] != 0:
            answer = index%n
            return answer + 1
        index += 1
        
food_times = list(map(int, input().split()))
k = int(input())
print(solution(food_times,k))'''

#7
'''while True:
    score = list(map(int, input()))
    if len(score) % 2 == 0:
        break

if sum(score[:int(len(score)/2)]) * 2 == sum(score):
    print('LUCKY')
else:
    print('READY')'''

#8
'''arr = list(map(str, input()))

alp_arr = []
val = 0
for i in arr:
    if i.isalpha():
        alp_arr.append(i)
    else:
        val += int(i)
alp_arr.sort()
if val != 0:
    alp_arr.append(str(val))

print(''.join(alp_arr))'''


