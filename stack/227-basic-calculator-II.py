'''Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''
class Solution:
    def calculate(self, s: str) -> int:
        operation = '+'
        current_num_string = ''

        stack = []

        def isOperation(c):
            match c:
                case '+':
                    return True
                case '-':
                    return True
                case '*':
                    return True
                case '/':
                    return True
                case _:
                    return False

        def processOperation():
            match operation:
                case '+':
                    stack.append(int(current_num_string))
                case '-':
                    stack.append(-1*int(current_num_string))
                case '*':
                    last_num = stack.pop()
                    stack.append(last_num * int(current_num_string))
                case '/':
                    last_num = stack.pop()
                    print(last_num)
                    print(last_num // int(current_num_string))
                    stack.append(int(last_num / int(current_num_string)))

        for c in s:
            if c == ' ':
                continue 
            elif isOperation(c):
                processOperation()
                operation = c
                current_num_string = ''
            elif c.isdigit():
                current_num_string += c
        
        processOperation()
        return sum(stack)