#include <iostream>
using namespace std;

int kuai_su_mi(long long b, long long base, long long p, long long k)
{
    // p==1是递归边界条件
    if (p == 1)
    {
        return b % k;
    }
    // p==0是程序输入的特殊情况
    if (p == 0)
    {
        return 1 % k;
    }
    // 两种情况递归
    if (p % 2 == 0)
    {
        b *= base;
        base *= base;
        base %= k;
        b %= k;
        p /= 2;
        return kuai_su_mi(b, base, p, k);
    }
    else
    {
        b *= base;
        p -= 1;
        b %= k;
        return kuai_su_mi(b, base, p, k);
    }
}

int main()
{
    long long b, p, k;
    cin >> b >> p >> k;
    long long base = b;
    cout << b << "^" << p << " mod " << k << "=" << kuai_su_mi(b, base, p, k);
    return 0;
}