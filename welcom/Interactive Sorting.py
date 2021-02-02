N, Q = map(int, input().split())
label_ful = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
label = label_ful[:N]
ans = []
base = label[0]
ans.append(base)
for i in range(1, N):
    print("?"+base,label[N])
    data = input()
    if data == ">":
        ans.append(label[N])
    else:
        ans.insert(0,label[N])
    base = label[N]
print("!"+",".join(ans))