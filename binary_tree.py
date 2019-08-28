class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)

    __repr__ = __str__

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, item):
        cur = Node(item)
        if self.root is None:
            self.root = cur
        else:
            queue = [self.root]
            while queue:
                new_queue = []
                for node in queue:
                    if node.left is None:
                        node.left = cur
                        return
                    if node.right is None:
                        node.right = cur
                        return
                    new_queue.append(node.left)
                    new_queue.append(node.right)
                queue = new_queue

    def get_parent(self, item):
        if not self.root or self.root.item == item:
            return None
        queue = [self.root]
        while queue:
            new_queue = []
            for node in queue:
                if node.left and node.left.item == item:
                    return node
                if node.right and node.right.item == item:
                    return node
                if node.left is not None:
                    new_queue.append(node.left)
                if node.right is not None:
                    new_queue.append(node.right)
            queue = new_queue
        return None

    def delete(self, item):
        if self.root is None:
            return False
        parent = self.get_parent(item)
        if parent:
            if parent.left and parent.left.item == item:
                del_node = parent.left
            else:
                del_node = parent.right
            if del_node.left is None:
                if parent.left and parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.left
            elif del_node.right is None:
                if parent.left and parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.right
            else:
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    tmp_next.left = del_node.left
                else:
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left and parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
            return True
        else:
            return False

    def show_tree(self):
        if self.root is None:
            return
        res = []
        queue = [self.root]
        while queue:
            new_queue = []
            temp = []
            for node in queue:
                temp.append(node)
                if node is not None:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            res.append(temp)
            queue = new_queue

        for line in res:
            for node in line:
                print(node, end=' ')
            print()

