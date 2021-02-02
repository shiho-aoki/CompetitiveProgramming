N, Y = map(int, input().split())
X = list(range(0,N+1))
display = 0
disp_x = 0
disp_y = 0
disp_z = 0
for x_i in X:
    y = list(range(0, N+1-x_i))
    for y_i in y:
        z_i = N - (x_i+y_i)
        total = 10000*x_i + 5000*y_i + 1000*z_i
        if int(total) == Y:
            display += 1
            disp_x = x_i
            disp_y = y_i
            disp_z = z_i
            break
        else:
            display += 0
if display != 0:
    print(str(disp_x)+" "+str(disp_y)+" "+str(disp_z))
else:
    print(str(-1)+" "+str(-1)+" "+str(-1))