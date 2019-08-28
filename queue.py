class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, val):
        cur = Node(val)
        if self.is_empty():
            self.head = self.rear = cur
        else:
            self.rear.next = cur
            self.rear = cur

    def dequeue(self):
        if self.is_empty():
            print('queue is empty.')
        else:
            res = self.head.val
            self.head = self.head.next
            return res

    def peek(self):
        if self.is_empty():
            print('queue is empty.')
            return None
        else:
            return self.head.val

    def print_queue(self):
        p = self.head
        myqueue = []
        while p:
            myqueue.append(p.val)
            p = p.next
        print(myqueue)
