#include <iostream>
#include <iomanip>
using namespace std;
int n, r, a[100];

bool isIn(int tmp, int *a)
{
    for (int i = 0; i < 100; i++)
    {
        if (tmp == a[i])
        {
            return true;
        }
    }
    return false;
}

void dfs(int k)
{
    if (k > r)
    {
        for (int i = 1; i <= r; i++)
        {
            cout << setw(3) << a[i];
        }
        cout << endl;
    }
    else
    {
        for (int i = 1; i <= n; i++)
        {
            if (isIn(i, a))
            {
                continue;
            }
            a[k] = i;
            dfs(k + 1);
        }
    }
}

int main()
{
    cin >> n >> r;
    dfs(1);
    return 0;
}