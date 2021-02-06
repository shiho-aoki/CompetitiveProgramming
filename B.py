N, X = map(int, input().split())
A = list(map(int, input().split()))
A_p = []
for a_i in A:
    if not(a_i == X):
        A_p.append(str(a_i))
A_prim = ' '.join(A_p)
print(A_prim)