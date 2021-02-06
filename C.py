H, W = map(int,input().split())
S_hw = []
S_cnt = []
for i in range(0,H):
    S_iw = list(input())
    S_hw.append(S_iw)
    cnt_b = 0
    for i in S_iw:
        if i =="#":
            cnt_b +=1
    S_cnt.append([cnt_b])
print(S_cnt)