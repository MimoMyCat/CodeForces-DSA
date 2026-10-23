t = int(input())
lst=[]
for i in range(t):
    n, k = map(int, input().split())
    max = 2 ** (n - k + 1) + 2 * (k - 1)

    lst.append(max)

for item in lst:
    print(item)

    