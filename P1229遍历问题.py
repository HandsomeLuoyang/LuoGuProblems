s1 = input()
s2 = input()

ans = 0
for i in range(len(s1)-1):
    tmp = s1[i] + s1[i+1]
    tmp = tmp[::-1]
    if tmp in s2:
        ans += 1

print(1<<ans)