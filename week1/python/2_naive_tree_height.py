from collections import defaultdict as dd


class Tree:
    def __init__(self, parents):
        self.parents = parents
        self.children = dd(list)

        for i in range(len(self.parents)):
            self.children[parents[i]].append(i)

    def viewTree(self):

        for i in self.children.keys():
            print(f'{i}: {self.children[i]}')


def level(tree, node, l=1):
    for parent in tree.children.keys():
        if node in tree.children[parent]:
            if parent == -1:
                return l
            return level(tree, parent, l+1)


def height(tree, n):
    leafs = []
    for i in range(n):
        if i not in tree.children.keys():
            leafs.append(i)

    h = 0
    for leaf in leafs:
        h = max(h, level(tree, leaf))
    return h


n = int(input())
parents = list(map(int, input().split()))
tree = Tree(parents)

# tree.viewTree()
print(height(tree, n))
