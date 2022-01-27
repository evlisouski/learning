from binarytree import tree, bst, Node, build


class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# создать дерево высотой от корня 4. is_perfect = False (неполное дерево)
a = tree(height=4, is_perfect=False)
print(a)

# создать бинарное дерево поиска
b = bst(height=3, is_perfect=True)
print(b)

# создание такого же дерева в ручную
c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
print(c)

# создание дерева на основе списка
d = build([7, 3, 11, 1, 5, 9, 3, None, 2, None])
print(d)
