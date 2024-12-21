import collections

class PostfixNotation:
    def __init__(self):
        self.queue = collections.deque()

    def infixToPostfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        postfix=[]
        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char in precedence:
                while self.queue and self.queue[-1] != '(' and precedence[self.queue[-1]] >= precedence[char]:
                    postfix.append(self.queue.pop())
                self.queue.append(char)
            elif char == '(':
                self.queue.append(char)
            elif char == ')':
                while self.queue and self.queue[-1] != '(':
                    postfix.append(self.queue.pop())
                self.queue.pop()
        while self.queue:
            postfix.append(self.queue.pop())
        return ''.join(postfix)
    


postfix = PostfixNotation()
expression = input("Enter an expression: ")
print(postfix.infixToPostfix(expression))
