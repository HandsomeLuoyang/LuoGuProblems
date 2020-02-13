# 给定一个数组，求出数组内的值得和为sum的所有相加方式
# 例如 [1,2,3,4,5] sum=10
# 1 2 3 4
# 1 4 5
# 2 3 5

# 输入方式，第一行输入一个数组的值， 第二行输入一个sum

cnt = 0


def print_(x: list, lmt: int):
    global target_list
    for i in range(lmt+1):
        if x[i]:
            print(target_list[i], end=" ")
    print("")


def digui(x: list, i: int, has: int, residue: int):
    global sum_, target_list, cnt
    cnt += 1
    if i >= len(target_list):
        return
    if has + target_list[i] == sum_:
        x[i] = True
        print_(x, i)
        x[i] = False

    elif (has + residue >= sum_) and (has + target_list[i] < sum_):
        x[i] = True
        digui(x, i+1, has + target_list[i], residue - target_list[i])
    if has + residue - target_list[i] > sum_:
        x[i] = False
        digui(x, i+1, has, residue-target_list[i])


target_list = [int(x) for x in input().split()]
sum_ = int(input())

x = list()
for i in range(len(target_list)):
    x.append(False)

residue = sum(target_list)
digui(x, 0, 0, residue)
print("次数：" + str(cnt))