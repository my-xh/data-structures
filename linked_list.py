class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, val):
        cur = Node(val)
        cur.next = self.head
        self.head = cur
        self.size += 1

    def insert_at_tail(self, val):
        if self.is_empty():
            self.add_at_head(val)
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            cur = Node(val)
            p.next = cur
            self.size += 1

    def insert_at(self, idx, val):
        if idx < 0 or idx > self.length():
            raise IndexError('index out of range.')
        if idx == 0:
            self.insert_at_head(val)
        elif idx == self.length():
            self.insert_at_tail(val)
        else:
            p = self.head
            for _ in range(idx - 1):
                p = p.next
            cur = Node(val)
            temp = p.next
            p.next = cur
            cur.next = temp
            self.size += 1

    def get_at(self, idx):
        if idx < 0 or idx >= self.length():
            raise IndexError('index out of range.')
        p = self.head
        for _ in range(idx):
            p = p.next
        return p.val

    def remove_at(self, idx):
        if idx < 0 or idx >= self.length():
            raise IndexError('index out of range.')
        if idx == 0:
            self.head = self.head.next
        else:
            p = self.head
            for _ in range(idx - 1):
                p = p.next
            p.next = p.next.next
        self.size -= 1

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def print_list(self):
        p = self.head
        while p:
            print('{} -> '.format(p.val), end='')
            p = p.next
        print('None')

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            node = cur.next
            cur.next = prev
            prev = cur
            cur = node
        self.head = prev

