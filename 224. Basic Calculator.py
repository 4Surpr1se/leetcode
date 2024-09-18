class Solution:
    # n = iter(range(0, 10))
    def calculate(self, s: str) -> int:
        return self.recur(s, 0)[1]

    def recur(self, s: str, index: int):
        s = s.replace(' ', '')  # todo убрать
        # n = next(self.n)
        stack = []
        continuous_number = False
        negative_state = False
        while index < len(s):
            symbol = s[index]
            if symbol.isdigit():
                if continuous_number:
                    stack[-1] += symbol
                else:
                    stack.append(symbol)
                continuous_number = True
            else:
                if symbol == '-':
                    if s[index + 1].isdigit():
                        stack.append('-' + s[index + 1])
                        index += 1
                        continuous_number = True
                    else:
                        negative_state = not negative_state
                        continuous_number = False
                elif symbol == '(':
                    index, res = self.recur(s, index + 1)
                    stack.append(res * (-(2 * negative_state - 1)))
                    negative_state = False
                    continuous_number = False
                elif symbol == ')':
                    return index, sum(list(map(int, stack)))
                else:
                    continuous_number = False
            index += 1
            # print(n, stack)

        return index, sum(map(int, stack))

# print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))
# # print('\')
# print(Solution().calculate("(1+(4+5+2)-3)+(6+8)")[1])
# (exec("print((1+(4+5+2)-3)+(6+8))"))
# print(Solution().calculate("2-1 - 2"))[1]
