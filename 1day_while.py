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
