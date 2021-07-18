# 3-1 그리디 거스름돈 문제
'''n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n//coin
    n %= coin

print(count)
'''

#3-2 그리디 큰 수의 법칙
'''def calMax(n, input_list):
    ans = 0
    count = 0

    if input_list.count(max(input_list)) > 1:
        return M * max(input_list)

    input_list.sort()
    max_num = input_list[n-1]
    max2_num = input_list[n-2]

    for i in range(M):
        if count != K:
            ans += max_num
            count += 1
        else:
             ans += max2_num
             count = 0
    return ans

N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))
print(calMax(N, input_list))'''

#3-3 숫자 카드게임
'''N, M = map(int, input().split())
mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))

'''
# 3-4 1이 될 때까지
'''n, k = map(int, input().split())
count = 0
while(n != 1):
    n = n/k if n/k == int(n/k) else n-1
    count +=1
print(count)'''
