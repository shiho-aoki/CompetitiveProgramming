V, T, S, D = map(int, input().split())
vt = V*T
vs = V*S
if vt <= D <= vs:
    print("No")
else:
    print("Yes")