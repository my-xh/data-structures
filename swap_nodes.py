#!/usr/bin/env python3
from linked_list import LinkedList

def swap_nodes(linklist, v1, v2):
    if v1 == v2:
        return
    prev_node1 = None
    prev_node2 = None
    nodes = [v1, v2]

    p = linklist.head
    while p and nodes:
        if v1 in nodes:
            if p.val != v1:
                prev_node1 = p
            else:
                nodes.remove(v1)
        if v2 in nodes:
            if p.val != v2:
                prev_node2 = p
            else:
                nodes.remove(v2)
        p = p.next

    if nodes:
        return

    if prev_node1 is None:
        node1 = linklist.head
        node2 = prev_node2.next
        linklist.head = node2
        prev_node2.next = node1
    else:
        node1 = prev_node1.next
        if prev_node2 is None:
            node2 = linklist.head
            linklist.head = node1
        else:
            node2 = prev_node2.next
            prev_node2.next = node1
        prev_node1.next = node2

    temp = node1.next
    node1.next = node2.next
    node2.next = temp


if __name__ == '__main__':
    linklist = LinkedList()
    for i in range(1, 6):
        linklist.insert_at_tail(i)
    linklist.print_list()
    swap_nodes(linklist, 1, 4)
    print('after swapping...')
    linklist.print_list()
