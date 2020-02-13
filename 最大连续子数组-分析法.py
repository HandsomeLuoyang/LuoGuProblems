# 此方法线性时间


# 输入一个数组
target_list = [int(x) for x in input().split()]

# 前缀和数组
sum_list = list()
tmp = target_list[0]
sum_list.append(tmp)
for i in range(1, len(target_list)):
    tmp += target_list[i]
    sum_list.append(tmp)

max1 = max(sum_list)

max2 = max1 - min(sum_list)

print(max1 if max1 > max2 else max2)