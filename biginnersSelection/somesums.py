N, A, B = map(int, input().split())
output = 0
for i in range(1,N+1):
    data_i = list(str(i))
    total = 0
    for data in data_i:
        total += int(data)
    if A <= total<=B:
        output += i

print(output)