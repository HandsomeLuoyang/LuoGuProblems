# Get two values
cpty = int(input())
cnt = int(input())

# Init the record list
f = list()
for i in range(0, 20006):
    f.append(0)

# Get the weight list
w = list()
w.append(0)
for i in range(1, cnt+1):
    tmp = int(input())
    w.append(tmp)

# Update the record list throught the weight list
for i in range(1, cnt+1):
    j = cpty
    while j >= w[i]:
        f[j] = max(f[j], f[j - w[i]] + w[i])
        j -= 1

# Print the answer
print(cpty - f[cpty])
