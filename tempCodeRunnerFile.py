# 动态规划
# for i in range(1, len1):
#     for j in range(1, len2):
#         if s1[i] == s2[j]:
#             lst_lst[i][j] = lst_lst[i-1][j-1] + 1
#             dire_lst[i][j] = "zuoshang"
#         else:
#             if lst_lst[i-1][j] >= lst_lst[i][j-1]:
#                 lst_lst[i][j] = lst_lst[i-1][j]
#                 dire_lst[i][j] = "shang"
#             else:
#                 lst_lst[i][j] = lst_lst[i][j-1]
#                 dire_lst[i][j] = "zuo"

# ss = ""

# # 反向寻找字符串，递归


# def digui_print(i, j):
#     global ss
#     if i < 0 or j < 0:
#         return
#     if dire_lst[i][j] == "zuo":
#         digui_print(i, j-1)
#     elif dire_lst[i][j] == "shang":
#         digui_print(i-1, j)
#     elif dire_lst[i][j] == "zuoshang" or dire_lst[i][j] == 1:
#         ss += s1[j]
#         digui_print(i-1, j-1)


# digui_print(len1-1, len2-1)

# print(ss[::-1])