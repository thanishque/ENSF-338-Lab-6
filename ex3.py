import sys

class Node:
    def __init__(self, value=None, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            return popped
        else:
            raise Exception("Stack is empty")

class ExpressionTree:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def higher_precedence(self, op1, op2):
        return self.precedence[op1] >= self.precedence[op2]

    def infix_to_postfix(self, expression):
        stack = []
        postfix = []
        for char in expression:
            if char.isdigit():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.higher_precedence(stack[-1], char):
                    postfix.append(stack.pop())
                stack.append(char)
        while stack:
            postfix.append(stack.pop())
        return postfix

    def build_tree(self, postfix):
        stack = Stack()
        for char in postfix:
            if char.isdigit():
                stack.push(Node(char))
            else:
                right_node = stack.pop()
                left_node = stack.pop()
                stack.push(Node(char, left=left_node, right=right_node))
        return stack.pop()

    def evaluate(self, root):
        if root.value.isdigit():
            return int(root.value)
        left_val = self.evaluate(root.left)
        right_val = self.evaluate(root.right)
        if root.value == '+':
            return left_val + right_val
        elif root.value == '-':
            return left_val - right_val
        elif root.value == '*':
            return left_val * right_val
        elif root.value == '/':
            return left_val / right_val

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <expression>")
        sys.exit(1)

    expression = sys.argv[1]

    tree = ExpressionTree()
    postfix = tree.infix_to_postfix(expression)
    root = tree.build_tree(postfix)
    result = tree.evaluate(root)
    print("Result:", result)

if __name__ == "__main__":
    main()


# references: https://www.geeksforgeeks.org/expression-tree/
# chat.openai.com
