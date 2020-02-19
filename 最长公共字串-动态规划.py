s1 = input()
s2 = input()
len1, len2 = len(s1), len(s2)

dp_matrix = list()
for i in range(len1+1):
    tmp = list()
    for j in range(len2+1):
        tmp.append(0)
    dp_matrix.append(tmp)

max_length = 0
max_string = ""

cnt = 0

for i in range(0, len1):
    for j in range(0, len2):
        if s1[i] == s2[j]:
            cnt += 1
            dp_matrix[i+1][j+1] = dp_matrix[i][j] + 1
        else:
            cnt += 1
            dp_matrix[i+1][j+1] = 0
        if dp_matrix[i+1][j+1] > max_length:
            max_length = dp_matrix[i+1][j+1]
            max_string = ""
            for k in range(max_length-1, -1, -1):
                cnt += 1
                max_string += s1[i-k]

# 打印矩阵
# for i in dp_matrix:
#     for j in i:
#         print(j, end=" ")
#     print("")

print("字符串长度：", len1)
print("最大长度：", max_length, " 字符串：", max_string)
print("运行次数：", cnt)

# 通过测试，最终算法的复杂度近似为n的平方,公共字串越长算法时间复杂度会变高但是这个变高是从n的平方变成2乘以n的平方，增长缓慢
