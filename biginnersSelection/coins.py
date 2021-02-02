a = int(input())
b = int(input())
c = int(input())
X = int(input())

A = list(range(0,a+1))
B = list(range(0,b+1))
C = list(range(0,c+1))

disc = []
disc.append({"500":A})
if len(B)<=len(C):
    if len(A)<=len(B):
        disc.append({"100":B})
        disc.append({"50":C})
    else:
        disc.insert(0,{"100":B})
        if len(A)<len(C):
            disc.append({"50":C})
        else:
            disc.insert(0,{"50":C})
else:
    if len(A)<len(C):
        disc.append({"50":C})
        disc.append({"100":B})
    else:
        disc.insert(0,{"50":C})
        if len(A)<len(B):
            disc.append({"100":B})
        else:
            disc.insert(0,{"100":B})

hit = 0
for l in list(disc[0].values())[0]:
    for m in list(disc[1].values())[0]:
        for n in list(disc[2].values())[0]:
            total = int(list(disc[0].keys())[0])*l+int(list(disc[1].keys())[0])*m+int(list(disc[2].keys())[0])*n
            if total == X:
                hit += 1
print(hit)