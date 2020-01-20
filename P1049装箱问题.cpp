#include <iostream>
#include <cstdio>
using namespace std;
int f[20005], w[35];
int main()
{
    int v, n;
    cin >> v >> n; // 输入v：总容量，n：物品个数
    for (int i = 1; i <= n; i++)
        cin >> w[i];             // 输入各个物品的重量
    for (int i = 1; i <= n; i++) // 从第一个物品开始记录重量
        for (int j = v; j >= w[i]; j--)  // 每一次都更新重量数组
            f[j] = max(f[j], f[j - w[i]] + w[i]);
    cout << v - f[v];
    return 0;
}