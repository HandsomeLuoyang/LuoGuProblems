def digui(l_start: int, r_start: int, ss: list) -> None:
    if l_start < 0:
        return
    ss[l_start], ss[r_start] = ss[r_start], ss[l_start]
    ss[l_start+1], ss[r_start+1] = ss[r_start+1], ss[l_start+1]
    for i in ss:
        print(i, end="")
    print("")
    if r_start > 8:
        r_start -= 2
    else:
        r_start -= 1
    ss[l_start], ss[r_start] = ss[r_start], ss[l_start]
    ss[l_start+1], ss[r_start+1] = ss[r_start+1], ss[l_start+1]
    for i in ss:
        print(i, end="")
    print("")
    if r_start > 7 or r_start < 6:
        l_start -= 1
    else:
        l_start -= 2
    digui(l_start, r_start, ss)


n = int(input())
ss = []

for i in range(n):
    ss.append("o")

for i in range(n):
    ss.append("*")

ss.append("-")
ss.append("-")

l_start = n-1
r_start = 2*n

for i in ss:
    print(i, end="")
print("")
digui(l_start, r_start, ss)
print("--", end="")
for i in range(n):
    print("o*", end="")
