import math
# TODO:没写好，等学成归来


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def digui(n):
    global ans
    for i in range(2, (n//2)+1):
        if is_prime(i) and is_prime(n-i):
            ans += 1
        digui(i)
        digui(n-i)


target = int(input())
ans = 1 if is_prime(target) else 0
digui(target)
print(ans)
