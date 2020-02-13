# 题目：对于长度为N的数组A，求子数组的和接近0的子数组，要求时间复杂度O(NlogN)

# 输入一个数组
target_list = [int(x) for x in input().split()]
# 从数组中选出最接近0的
min_ = sorted(target_list, key=lambda x: abs(x))[0]

# 首先开一个相等长度的数组，存储从0到i的和的值
sum_list = list()
sum_ = 0

for i in target_list:
    sum_ += i
    sum_list.append(sum_)
sum_list.sort()

other_min = sorted(sum_list, key=lambda x: abs(x))[0]
for i in range(len(target_list)-1):
    other_min = other_min if abs(other_min) < (
        sum_list[i+1] - sum_list[i]) else (sum_list[i+1] - sum_list[i])

print(min_ if abs(min_) < other_min else other_min)