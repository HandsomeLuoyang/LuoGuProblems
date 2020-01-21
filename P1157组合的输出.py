global n, r
global a
a = [0 for i in range(20)]
n = 0
r = 0

def dfs(k):
    global n, r, a
    if int(k) > r:
        for i in range(1, r+1):
            print("%3d" % a[i], end="")
        print("")
        return 
    else:
        for i in range(a[k-1]+1, n+1):
            a[k] = i
            dfs(k+1)



def main():
    global n, r
    n, r = [int(x) for x in input().split()]
    dfs(1)

main()
