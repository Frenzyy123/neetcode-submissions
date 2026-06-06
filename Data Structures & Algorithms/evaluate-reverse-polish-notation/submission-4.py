class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operands = {'+','-','/','*'}
        for token in tokens:
            if token in operands:
                second_num = stack.pop()
                first_num = stack.pop()
                if token == '+':
                    stack.append(first_num + second_num)
                elif token == '-':
                    stack.append(first_num - second_num)
                elif token == '/':
                    sol = first_num // second_num
                    if first_num < 0 and second_num > 0 or first_num > 0 and second_num < 0:
                        if first_num % second_num != 0:
                            sol += 1
                    stack.append(sol)
                elif token == '*':
                    stack.append(first_num * second_num)
                continue
            stack.append(int(token))
        return stack.pop()
