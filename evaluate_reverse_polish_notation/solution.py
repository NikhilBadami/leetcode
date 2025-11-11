class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Need to evaluate a mathematical expression in reverse polish notation where valid operations are addition,
        subtraction, multiplcation and division. Based on the examples, for each operand found, I evaluate the two most
        recent numbers in the list. This could be represented as a stack, i.e., FIFO. As I operate along the input list,
        I store the numbers in a stack and as I come across the special operation characaters, I pop off a certain number
        of numbers from the stack to do the operation. Each operand in the equation may be an interger or another
        expression i.e., 3 or (9+5). Division is always floored

        How many numbers should be removed from the stack? Also, what to do with the running result? For the result,
        it should be put back onto the stack once its been computed. Then, for each operand encountered, remove the
        top two numbers on the stack and evaluate using the operand found. The first number popped is to the right of
        the operand and the second number is to the left.

        Edge cases:
        Input of 1: return the input (note an input of two with no operand is not valid. Additionally, each operator
        must have 2 operands)

        time: O(n)
        memory: O(n) worst case
        """
        import math

        if len(tokens) == 1:
            return int(tokens[0])
        
        operators = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t in operators:
                # Get two operands
                right = int(stack.pop())
                left = int(stack.pop())
                if t == '+':
                    stack.append(left + right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '*':
                    stack.append(left * right)
                else:
                    stack.append(math.trunc(left / right))
            else:
                stack.append(t)

        # There should only be one value in the stack, the result
        return stack[-1]
        
