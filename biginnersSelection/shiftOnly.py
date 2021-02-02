N = int(input())
data = list(map(int, input().split()))
def oOrE(data:list):
    for i in data:
        if (i%2) != 0:
            res="o"
            break
        else:
            res ="e"
    return res
def calc_cut(n):
    return n/2

min_ = min(data)
i = 0
while (min_%2) == 0:
    flag = oOrE(data)
    if flag == "o":
        break
    else:
        data=list((map(calc_cut, data)))
        i += 1

print(i)