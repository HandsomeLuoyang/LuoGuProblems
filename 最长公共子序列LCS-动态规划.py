s1 = input()
s2 = input()

len1, len2 = len(s1), len(s2)

# 长度数组
lst_lst = list()
# 方向数组
dire_lst = list()

# 初始化长度数组和方向数组，方向数组随便初始化，有那个大小就行了
for i in range(len1):
    tmp_lst = list()
    for j in range(len2):
        if i==0 or j==0:
            if s1[i] != s2[j]:
                tmp_lst.append(0)
            else:
                tmp_lst.append(1)
        else:
            tmp_lst.append(0)
    lst_lst.append(tmp_lst)
    dire_lst.append(tmp_lst[:])


# 动态规划
for i in range(1, len1):
    for j in range(1, len2):
        if s1[i] == s2[j]:
            lst_lst[i][j] = lst_lst[i-1][j-1] + 1
            dire_lst[i][j] = "zuoshang"
        else:
            if lst_lst[i-1][j] >= lst_lst[i][j-1]:
                lst_lst[i][j] = lst_lst[i-1][j]
                dire_lst[i][j] = "shang"
            else:
                lst_lst[i][j] = lst_lst[i][j-1]
                dire_lst[i][j] = "zuo"

ss = ""

# 反向寻找字符串，递归


def digui_print(i, j):
    global ss
    if i < 0 or j < 0:
        return
    if dire_lst[i][j] == "zuo":
        digui_print(i, j-1)
    elif dire_lst[i][j] == "shang":
        digui_print(i-1, j)
    elif dire_lst[i][j] == "zuoshang" or dire_lst[i][j] == 1:
        ss += s1[j]
        digui_print(i-1, j-1)


digui_print(len1-1, len2-1)

print(ss[::-1])
