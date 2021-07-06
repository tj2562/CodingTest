#11654
'''
ipt = input()
try:
    print(ord(ipt))
except:
    print(chr(int(ipt)))
'''
#11720
'''
num = int(input())
mem = int(input())
sum_num = sum(list(map(int, str(mem))))
print(sum_num)

'''
#10809
'''
lower_case = list(map(str, 'abcdefghijklmnopqrstuvwxyz'))
S = list(map(str, input()))
ans = [S.index(x) if x in S else -1 for x in lower_case]
print(" ".join(list(map(str, ans))))
'''
#2675
t = int(input())
for i in range(t):
    seq, s = input().split()
    text = ''
    for j in s:
        for k in range(int(seq)):
            text += (j)
    print(text)
    text = ''
