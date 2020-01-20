#include <iostream>
#include <string>
using namespace std;


void dfs(string in, string after)
{
    if (in.size() > 0)
    {
        char ch = after[after.size()-1];
        int index = in.find(ch);
        cout<<ch;
        dfs(in.substr(0, index), after.substr(0, index));
        dfs(in.substr(index+1), after.substr(index, in.size()-1-index));
    }
}



int main()
{
    string after;
    string in;
    cin>>in>>after;
    dfs(in, after);
    return 0;
}