n = int(input())
l = list(map(int, input().split()))
m = int(input())

for i in range(1, n-m+2):
    print(max(l[i-1:i+m-1]), end = ' ')