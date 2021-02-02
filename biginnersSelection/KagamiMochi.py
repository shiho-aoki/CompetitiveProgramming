N = int(input())
d = []
for i in range(0,N):
    d_i = int(input())
    d.append(d_i)
d_sort = set(sorted(d))
print(len(d_sort))