#4673 셀프넘버
'''
def cal(num):
    d_n = num + sum(map(int, str(num)))
    return d_n

d_n_list = []
for i in range (1, 10001):
    d_n_list.append(cal(i))

ans = list(set(range(1,10001)) - set(d_n_list))
ans.sort()
for x in ans:
    print(x)
'''
#1065 한수
input_num = int(input())
dif_list = []
count = 0
for x in range(1,input_num+1):
    num_list = list(map(int, str(x)))
    for i in len(num_list)-1:
        dif_list.append(num_list[i+1] - num_list[i])
    if len(set(dif_list)) == 1:
        count += 1
        ''''''