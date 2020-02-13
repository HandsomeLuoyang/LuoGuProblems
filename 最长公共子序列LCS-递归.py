s1 = input()
s2 = input()

i = 0
def digui(s1, s2):
    global i
    i += 1
    
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + digui(s1[:-1], s2[:-1])
    else:
        return max(digui(s1[:-1], s2[:]), digui(s1[:], s2[:-1]))

print(digui(s1, s2))
print(i)