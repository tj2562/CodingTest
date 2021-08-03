'''# 순차 탐색
def sequential_search(n,target,array):
    for i in range(n):
        if array[i] == target:
            return i+1
input_data = input().split()
n = int(input_data[0])
target = input_data[1] # 찾고자 하는 문자열
array = input().split()

print(sequential_search(n,target,array))'''

'''#이진탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array, target, mid+1, end)

 #원소의 개수와 target 입력받기
n, target = list(map(int, input().split()))
 #전체 원소 입력받기
array = list(map(int,input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
'''

#이진 탐색 트리
'''
import sys
input_data = sys.stdin.readline().rstrip() #문자열 한줄로 입력받기, 시간 초과를 피할 수 있다.'''

#문제2_부품찾기
 #이진탐색
'''def binary_search(array, target, start, end):
    mid = (start + end)//2
    if start > end:
        return None
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
target_list = list(map(int, input().split()))

for i in range(m):
    if binary_search(array, target_list[i], 0, n-1) == None:
        print("no", end= " ")
    else:
        print("yes", end= " ")'''

'''n = int(input())
array = [0] * 100001
for i in input.split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end= " ")
    else:
        print("no", end= " ")
'''

n, x = map(int,input().split())
def binary_search(array, target, start, end):
    mid = (start + end)//2
    if start > end:
        return None
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
