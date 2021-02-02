S = input()
t = S
replace_list = ["dreameraser", "dreamerase", "dreamer", "eraser", "erase", "dream"]
for rl in replace_list:
    t = t.replace(rl, " ")

length = len(list(set(t)))
if length != 1:
    print("NO")
else:
    print("YES")