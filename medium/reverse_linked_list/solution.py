class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def push_front(head: Node, val: int) -> Node:
    node = Node(val)
    node.next = head
    head = node
    return head

def push_back(head: Node, val: int) -> Node:
    if head is None:
        push_front(head, val)
    node = Node(val)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = node
    return head

def print_list(head: Node):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next

def reverse_linked_list(head: Node) -> Node:
    if head is None or head.next is None:
        return head
    prev_node = None
    curr_node = head
    next_node = head
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node

if __name__ == "__main__":
    list1 = push_front(None, 1)
    list1 = push_front(list1,2)
    list1 = push_front(list1,3)
    list1 = push_front(list1,4)
    list1 = push_front(list1,5)
    print("List before reversing:")
    print_list(list1)
    print("List after reversing")
    list1 = reverse_linked_list(list1)
    print_list(list1)