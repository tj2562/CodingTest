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
'''t = int(input())
for i in range(t):
    seq, s = input().split()
    text = ''
    for j in s:
        for k in range(int(seq)):
            text += (j)
    print(text)
    text = '''
#1157
'''def most_frequent(data):
    cnt = []
    text = list(set(data))
    for x in text:
        cnt.append(data.count(x))
    return text[cnt.index(max(cnt))] if cnt.count(max(cnt)) == 1 else '?'

t = list(map(str, input().upper()))
print(most_frequent(t))'''
#1152
'''
input_text = list(input().split())
print(len(input_text))'''
#2908
'''input_text = input()
rvs_text = list(map(int, ''.join(reversed(input_text)).split()))
print(max(rvs_text))'''
#

