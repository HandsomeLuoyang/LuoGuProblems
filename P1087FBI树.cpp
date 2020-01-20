#include <iostream>
#include <string>
using namespace std;

struct node
{
    string value;
    struct node *left;
    struct node *right;
    node(string s)
    {
        value = s;
        left = NULL;
        right = NULL;
    }
};

string judge_string(string tmp)
{
    if (tmp.size() > 0 && tmp.find("1") == string::npos)
    {
        return "B";
    }
    else if (tmp.size() > 0 && tmp.find("0") == string::npos)
    {
        return "I";
    }
    else
    {
        return "F";
    }
}

void build_tree(string org, node *root)
{
    // 字符串分割成左右两部分
    int length = org.size();
    if (length < 2)
    {
        return;
    }
    string lft = org.substr(0, length / 2);
    string rht = org.substr((length / 2), length / 2);
    // cout << "left: " << judge_string(lft) << " right: " << judge_string(rht) << endl;

    // 左右节点创建连接
    root->left = new node(judge_string(lft));
    root->right = new node(judge_string(rht));

    // 边界判定
    if (lft.size() > 1 && rht.size() > 1)
    {
        build_tree(lft, root->left);
        build_tree(rht, root->right);
    }
}

void pastTraverse(node *nd)
{
    // cout << nd->value;
    if (nd->left != NULL)
        pastTraverse(nd->left);
    if (nd->right != NULL)
        pastTraverse(nd->right);
    cout << nd->value;
}

int main()
{
    int n;
    cin >> n;
    string org;
    cin >> org;
    node *root = new node(judge_string(org));
    build_tree(org, root);
    pastTraverse(root);
    return 0;
}
