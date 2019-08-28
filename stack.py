class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
        else:
            self.stack.append(data)

    def pop(self):
        if not self.stack:
            # raise IndexError('pop from an empty stack')
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print('an empty stack')

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()

    def show(self):
        for i in reversed(self.stack):
            print('|{:^3d}|'.format(i))
        print('=====')
