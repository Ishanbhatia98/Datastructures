import sys
sys.setrecursionlimit(10**7)


class Tree:
    def __init__(self, n, parents):
        self.n = n
        self.parents = parents

    def height(self):
        heights = [0 for _ in range(self.n)]
        for vertex in range(self.n):
            if(heights[vertex] != 0):
                continue
            height = 0
            i = vertex
            while i != -1:
                if(heights[i] != 0):
                    height += heights[i]
                    break
                height += 1
                i = self.parents[i]
            i = vertex
            while i != -1:
                if heights[i] != 0:
                    break
                heights[i] = height
                height -= 1
                i = self.parents[i]
        return max(heights)


n = int(input())
parents = list(map(int, input().split()))

tree = Tree(n, parents)

print(tree.height())
