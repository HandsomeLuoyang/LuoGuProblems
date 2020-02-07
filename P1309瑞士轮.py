import functools
def cmp(x:list, y:list):
    if x[1] > y[1]:
        return -1
    elif x[1] < y[1]:
        return 1
    else:
        if x[0] < y[0]:
            return -1
        else:
            return 1


def pk(list_index_score, dic_index_power):
    i = 0
    while i < len(list_index_score)-1:
        if dic_index_power[list_index_score[i][0]] > dic_index_power[list_index_score[i+1][0]]:
            list_index_score[i][1] += 1
        else:
            list_index_score[i+1][1] += 1
        i += 2


N, R, Q = [int(x) for x in input().split()]
score_list = [int(x) for x in input().split()]
power_list = [int(x) for x in input().split()]

list_index_score = []
for i in range(0, len(score_list)):
    tmp = [i+1, score_list[i]]
    list_index_score.append(tmp)

dic_index_power = {}
for i in range(0, len(power_list)):
    dic_index_power[i+1] = power_list[i]

list_index_score.sort(key=functools.cmp_to_key(cmp))

for i in range(R):
    pk(list_index_score, dic_index_power)
    list_index_score.sort(key=functools.cmp_to_key(cmp))

print(list_index_score[Q-1][0])


