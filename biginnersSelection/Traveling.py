N = int(input())
T = []
X = []
Y = []
for i in range(0, N):
    t_i, x_i, y_i = map(int, input().split())
    T.append(t_i)
    X.append(x_i)
    Y.append(y_i)
t_base = 0
x_base = 0
y_base = 0
ng = 0
for x, y ,t in zip(X,Y,T):
    if t-t_base == (x-x_base)+(y-y_base):
        t_base = t
        x_base = x
        y_base = y
    elif t -t_base > (x-x_base)+(y-y_base):
        check = (t-t_base) - ((x-x_base)+(y-y_base))
        if t-t_base %2 !=0:
            if check %2 ==0:
                t_base = t
                x_base = x
                y_base = y
            else:
                ng +=1
                break
        else:
            if check %2 !=0:
                t_base =t
                x_base =x
                y_base =y
            else:
                ng +=1
                break
    else:
        ng +=1
        break
if ng == 0:
    print("Yes")
else:
    print("No")