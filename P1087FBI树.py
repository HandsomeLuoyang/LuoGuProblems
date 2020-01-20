class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def pastTraverse(self):
        if self.left != None:
            self.left.pastTraverse()
        if self.right != None:
            self.right.pastTraverse()
        print(self.value, end="")


def judge_string(ss):
    if not "1" in ss:
        return "B"
    if not "0" in ss:
        return "I"
    return "F"


def build_tree(org:str, root:Node)->None: 
    length = len(org)
    if length < 2:
        return
    lft = org[:length//2]
    rht = org[length//2:]
    root.left = Node(judge_string(lft))
    root.right = Node(judge_string(rht))
    if len(lft) > 1 and len(rht) > 1:
        build_tree(lft, root.left)
        build_tree(rht, root.right)


def main():
    gbg = input()  # 这个值可以不要
    del gbg
    org = input().strip()  # 这是输入进来的字符串
    root = Node(judge_string(org))
    build_tree(org, root)
    root.pastTraverse()

main()
