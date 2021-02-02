N = int(input())
a = list(map(int,input().split()))
data = sorted(a, reverse=True)
Alice = 0
Bob = 0
for i in range(0, len(data)):
    if i%2 != 0:
        Bob += data[i]
    else:
        Alice += data[i]
print(Alice-Bob)