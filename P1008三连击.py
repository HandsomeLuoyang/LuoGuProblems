def judge(i, j, k):
    flag1 = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + \
        int(str(j)[0]) + int(str(j)[1]) + int(str(j)[2]) + \
        int(str(k)[0]) + int(str(k)[1]) + int(str(k)[2]) == 45
    
    flag2 = int(str(i)[0]) * int(str(i)[1]) * int(str(i)[2]) * \
        int(str(j)[0]) * int(str(j)[1]) * int(str(j)[2]) * \
        int(str(k)[0]) * int(str(k)[1]) * int(str(k)[2]) == 362880
    
    if flag1 and flag2:
        return True
    else:
        return False



def main():
    for i in range(123, 333):
        j = 2 * i
        k = 3 * i
        if judge(i, j, k):
            print(str(i) + " " + str(j) + " " + str(k))


main()
