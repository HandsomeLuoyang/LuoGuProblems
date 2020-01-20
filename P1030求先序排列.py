def dfs(in_, after):
    if len(in_) > 0:
        ch = after[len(after)-1]
        index = in_.find(ch)
        print(ch, end="")
        dfs(in_[:index], after[:index])
        dfs(in_[index+1:], after[index:index+len(in_[index+1:])])

in_ = input()
after = input()
dfs(in_, after)