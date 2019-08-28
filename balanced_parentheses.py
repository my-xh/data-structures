#!/usr/bin/env python3
from stack import Stack

def is_balanced(strings):
    stack = Stack(len(strings))

    for s in strings:
        if s == '(':
            stack.push(s)
        elif s == ')':
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()


if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    for example in examples:
        print('{}: {}'.format(example, is_balanced(example)))
