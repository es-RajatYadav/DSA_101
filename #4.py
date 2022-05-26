class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(temp, data):
    que = []
    que.append(temp)
    while len(que):
        temp = que[0]
        que.pop(0)
        if not temp.left:
            if data is not None:
                temp.left = TreeNode(data)
            else:
                temp.left = TreeNode(0)
            break
        else:
            que.append(temp.left)
            if not temp.right:
                if data is not None:
                    temp.right = TreeNode(data)
                else:
                    temp.right = TreeNode(0)
                break
            else:
                que.append(temp.right)


def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    return Tree


class Solution(object):
    def lCA(self, root, p, q):
        if not root:
            return None
        if root.data == p or root.data == q:
            return root
        left = self.lCA(root.left, p, q)
        right = self.lCA(root.right, p, q)
        if right and left:
            return root
        return right or left


ob1 = Solution()
Str = input()
arrayStr = Str.split(",")
intArray = list(map(int, arrayStr))
tree = make_tree(intArray)
x = int(input())
y = int(input())
print(ob1.lCA(tree, x, y).data)
