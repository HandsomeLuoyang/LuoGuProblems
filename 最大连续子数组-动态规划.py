# 输入一个数组
target_list = [int(x) for x in input().split()]


sum_ = target_list[0]
result = target_list[0]

for i in range(1, len(target_list)):
    if sum_ > 0:
        sum_ += target_list[i]
    else:
        sum_ = target_list[i]

    if sum_ > result:
        result = sum_

print(result)

