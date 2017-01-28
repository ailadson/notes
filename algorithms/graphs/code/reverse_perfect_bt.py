def reverse_perfect_bt(node, to_reverse = True):
    if node.right_child is None:
        return
    if to_reverse:
        r_child = node.right_child
        l_child = node.left_child
        node.right_child, node.left_child = l_child, r_child
        r_child.right_child, l_child.right_child = l_child.right_child, r_child.right_child
        r_child.left_child, l_child.left_child = l_child.left_child, r_child.left_child
    reverse_perfect_bt(node.right_child, not to_reverse)
    reverse_perfect_bt(node.left_child, not to_reverse)

class Node:
    count = 1
    def __init__(self):
        self.count = Node.count
        self.right_child = None
        self.left_child = None
        Node.count += 1

    def traverse(self):
        if self.left_child:
            self.left_child.traverse()
        print self
        if self.right_child:
            self.right_child.traverse()

    def __str__(self):
        return "{}".format(self.count)

    def __repr__(self):
        return self.__str__(self)

n1 = Node()
n2 = Node()
n3 = Node()
n1.left_child = n2
n1.right_child = n3
n4 = Node()
n5 = Node()
n2.left_child = n4
n2.right_child = n5
n6 = Node()
n7 = Node()
n3.left_child = n6
n3.right_child = n7

n1.traverse()
reverse_perfect_bt(n1)
print "-"*9
n1.traverse()
