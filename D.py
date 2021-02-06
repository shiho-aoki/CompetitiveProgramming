x,y,R = map(float,input().split())
left = R**2
rights = []
for X in range(int(x-R),int(x+R+1)):
    for Y in range(int(y-R),int(y+R+1)):
        right = (X-x)**2 + (Y-y)**2
        rights.append(right)

rights.sort()
for i in rights:
    if i > left:
        a= i
        break
print(rights.index(a))