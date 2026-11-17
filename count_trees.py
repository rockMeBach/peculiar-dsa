# count structurally-unique binary trees with N nodes
# could be solved using the Catalan formula too

def countTrees(n):
    if n <= 1:
        return 1  # empty tree counts as 1 way

    ways = 0
    for i in range(n):
        ways += countTrees(i) * countTrees(n - 1 - i)
    return ways

print(countTrees(4))  # 14