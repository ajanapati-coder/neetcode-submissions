import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': None
        }
        
        numbersStack = []

        for c in tokens:
            if c not in operators:
                numbersStack.append(int(c))
            elif c == "/":
                first = numbersStack.pop()
                second = numbersStack.pop()
                result = int(second / first)
                numbersStack.append(result)
            else:
                first = numbersStack.pop()
                second = numbersStack.pop()
                result = operators[c](second, first)
                numbersStack.append(result)
        
        return numbersStack[0]
