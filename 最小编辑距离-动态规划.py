s1 = input()
s2 = input()

len1, len2 = len(s1), len(s2)

# 长度数组
lst_lst = list()

# 初始数组
for i in range(len1+1):
    tmp_lst = list()
    for j in range(len2+1):
        if i == 0:
            tmp_lst.append(j)
        elif j == 0:
            tmp_lst.append(i)
        else:
            tmp_lst.append(0)
    lst_lst.append(tmp_lst)

for i in range(0, len1):
    for j in range(0, len2):
        if s1[i] == s2[j]:
            lst_lst[i+1][j+1] = lst_lst[i][j]
        else:
            lst_lst[i+1][j+1] = min(lst_lst[i][j+1],
                                lst_lst[i+1][j],
                                lst_lst[i][j]) + 1

for i in lst_lst:
    for j in i:
        print("%5d" % j, end="")
    print("")

print("最小编辑长度为：", lst_lst[len1][len2])
