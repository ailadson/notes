class AVL:
    def __init__(self):
        self.root = self.new_node(None)

    def traverse(self, root, indent = 0):
        print root
        if root.get('key') is None:
            return

        self.traverse(root['left_child'], indent + 1)
        print "{}{}".format("-" * indent, root['key'])
        self.traverse(root['right_child'], indent + 1)


    def insert(self, val):
        node = self.root

        while node.get('key') is not None:
            if val > node.get('key'):
                node = node.get('right_child')
            else:
                node = node.get('left_child')

        node['key'] = val
        node['right_child'] = self.new_node(None, node)
        node['left_child'] = self.new_node(None, node)

        self.preserve_avl_property(node)

    def preserve_avl_property(self, node):
        while True:
            left_height, right_height = self.calc_height(node)
            height_diff = right_height - left_height

            if abs(height_diff) > 1:
                if height_diff > 0: # right heavy
                    self.right_heavy_rotation(node, right_height, left_height)
                else: #left heavy
                    self.left_heavy_rotation(node, right_height, left_height)

            node = node.get('parent')

            if node is None:
                return

    def calc_height(self, node):
        right_child = node['right_child']
        left_child = node['left_child']

        if right_child is None:
            right_height = -2
            left_height = -2
        else:
            right_height = right_child['h']
            left_height = left_child['h']

        node['h'] = 1 + max(right_height, left_height)
        return [left_height, right_height]

    def right_heavy_rotation(self, node, r_height, l_height):
        if r_height >= l_height:
            self.rotate_right(node)
        else:
            self.rotate_right(node.get('right_child'))
            self.rotate_left(node)

    def left_heavy_rotation(self, node, r_height, l_height):
        if l_height >= r_height:
            self.rotate_left(node)
        else:
            self.rotate_left(node.get('left_child'))
            self.rotate_right(node)

    def rotate_right(self,node):
        parent = node.get('parent')
        left_child = node.get('left_child')

        if parent is not None:
            if node.get('key') > parent.get('key'):
                parent['right_child'] = left_child
            else:
                parent['left_child'] = left_child

        node['parent'] = left_child
        left_child['parent'] = parent

        left_child['right_child']['parent'] = node
        node['left_child'] = left_child['right_child']
        left_child['right_child'] = node

        self.calc_height(node)
        self.calc_height(left_child)

    def rotate_left(self, node):
        parent = node.get('parent')
        right_child = node.get('right_child')
        # print "=" * 10
        # print right_child

        if parent is not None:
            if node.get('key') > parent.get('key'):
                parent['right_child'] = right_child
            else:
                parent['left_child'] = right_child

        node['parent'] = right_child
        right_child['parent'] = parent

        if right_child['left_child'] is not None:
            right_child['left_child']['parent'] = node

        node['right_child'] = right_child['left_child']
        right_child['left_child'] = node

        self.calc_height(node)
        self.calc_height(right_child)


    def new_node(self, key, parent = None):
        return {
            'key' : key,
            'right_child' : None,
            'left_child' : None,
            'h' : -1,
            'parent' : parent
        }


a = AVL()
a.insert(10)
a.insert(9)
a.insert(8)
a.traverse(a.root)
# print a.root
