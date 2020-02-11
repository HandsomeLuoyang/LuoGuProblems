# 输入一个数组
target_list = [int(x) for x in input().split()]

## 检测次数
tt = 0
def max_sub_sum(a: list, bg: int, end: int) -> int:
    global tt
    tt += 1
    # 终止条件
    if bg == end:
        return a[bg]
    middle = (bg + end) // 2
    # 左右分治
    m1 = max_sub_sum(a, bg, middle)
    m2 = max_sub_sum(a, middle+1, end)

    # 找左边序列的最大后缀
    left = now = a[middle]
    for i in range(middle-1, bg-1, -1):
        now += a[i]
        left = max(left, now)
    # 找右边序列的最大前缀
    right = now = a[middle+1]
    for i in range(middle + 2, end+1):
        now += a[i]
        right = max(right, now)
    m3 = left + right
    # 三者中取最大值 
    return max(m1, m2, m3)

print(max_sub_sum(target_list, 0, len(target_list)-1))
print(tt)