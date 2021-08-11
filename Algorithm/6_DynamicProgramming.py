'''x = int(input())

d = [0] * x
d[0] = 0

for i in range(1,x):
    prev = []
    if i % 5 == 0:
        prev.append(d[i//5])
    elif i % 3 == 0:
        prev.append(d[i//3]) 
    elif i % 2 == 0:
        prev.append(d[i//2])
    prev.append(d[i-1])
    d[i] = min(prev)+1

print(d[x-1])'''
