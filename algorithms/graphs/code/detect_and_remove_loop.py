def remove_cycle_from_ll(head):
    fast = head
    slow = head

    if detect_cycle(slow, fast) is False:
        return False

    slow = head
    remove_cycle(slow, fast)
    return True

def detect_cycle(slow, fast):
    fast = fast.next

    while fast is not None and fast is not slow:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next

    return (fast is slow)

def remove_cycle(start, mid):
    while True:
        start = start.next
        if mid.next is start:
            mid.next = None
            return
        mid = mid.next


class Node:
    num = 0

    def __init__(self, val = None):
        self.num = Node.num
        self.next = val
        Node.num+=1

    def __str__(self):
        return "{}".format(self.num)

    def __repr__(self):
        return self.__str__(self)

node8 = Node()
node7 = Node(node8)
node6 = Node(node7)
node5 = Node(node6)
node4 = Node(node5)
node3 = Node(node4)
node2 = Node(node3)
node1 = Node(node2)
node8.next = node6

print detect_cycle(node1, node1)
print remove_cycle_from_ll(node1)
print detect_cycle(node1, node1)
