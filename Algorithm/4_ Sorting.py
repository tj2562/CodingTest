# 정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것
# 일반적으로 ㅁ누제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨

# 1_선택정렬
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꿈

'''array = [7,5,9,0,3,1,6,2,4,8]

for i in range(array):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    #파이썬에서는 한줄로 swaping 가능
    array[i], array[min_index] = array[min_index], array[i]
print(array)'''

# 선택 정렬의 시간 복잡도
# N + N-1 + N-2 + ~ + 2 = (N^2 + N -2) = O(N^2)

# 2_삽입 정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
# 앞의 데이터가 정렬되어있다고 판단하고 해당 인덱스의 원소를 알맞은 위치에 삽입
'''array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
'''

#3_ 퀵정렬
'''array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start>=end:  #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left<=right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left+=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right]>=array[pivot]):
            right-=1
        if(left>right): #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot]=array[pivot],array[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1,end)

quick_sort(array, 0, len(array)-1)
print(array)

# 파이썬의 장점을 살린 방식
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array)<=1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side=[x for x in tail if x<=pivot] #분할된 왼쪽 부분
    right_side=[x for x in tail if x>pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
#실행 결과[1,2,3,4,5,6,7,8,]
'''

# 4_계수정렬
'''
#모든 원소의 값이 0보다 크거나 같다고 가정
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):#리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i,end='') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

#실행 결과 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9'''

'''n, k = map(int,input().split())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
A.sort(), B.sort(reverse=True)
for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))'''

'''# 2_위에서 아래로
n = int(input())
nlist = []
for i in range(n):
    nlist.append(int(input()))
nlist.sort(reverse=True)
for i in range(n):
    print(nlist[i], end=' ')'''

#3_성적이 낮은 순서대로 학생 출력하기
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')

#4_두 배열의 원소 교체
