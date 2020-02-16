ss = input()

max_length = 1
now_length = 1
ch = ss[0]

now_ss = ss[0]
max_ss = ss[0]


for i in range(1, len(ss)):
    if ss[i] > ch:
        now_length += 1
        ch = ss[i]
        now_ss += ch
    else:
        now_length = 1
        ch = ss[i]
        now_ss = ch
    if now_length > max_length:
        max_length = now_length
        max_ss = now_ss
    # max_length = max(max_length, now_length)

print(max_length)
print(max_ss)

