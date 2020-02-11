# 输入一个数组
target_list = [int(x) for x in input().split()]
length = len(target_list)

def normal():
    global target_list, length
    maxsum = target_list[0]
    tt = 0
    x = y = 0
    for i in range(length):
        for j in range(i, length):
            cursum = 0
            for k in range(i, j+1):
                cursum += target_list[k]
                tt +=1
            if cursum > maxsum:
                x = i
                y = j+1
                maxsum = cursum

    print(maxsum)
    print(target_list[x:y])
    print("次数:", tt)

def youhua():
    """稍微优化一下暴力方法"""
    global target_list, length
    tt = 0
    max_list = []
    for i in range(length):
        max_sum = target_list[i]
        curmax = 0
        for j in range(i, length):
            tt += 1
            curmax += target_list[j]
            if curmax > max_sum:
                max_sum = curmax
        max_list.append(max_sum)

    print(max(max_list))
    print(tt)

# normal()
youhua()
