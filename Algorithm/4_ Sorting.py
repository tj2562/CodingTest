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

