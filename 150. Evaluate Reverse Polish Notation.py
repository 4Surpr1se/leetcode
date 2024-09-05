class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        pos = 0
        while len(tokens) > 1:
            if not tokens[pos].lstrip("-").isdigit():
                res = int(eval(f'{tokens[pos-2]} {tokens[pos]} {tokens[pos-1]}'))
                tokens[pos-2] = str(res)
                del tokens[pos], tokens[pos-1]
                pos -= 2
            else:
                pos += 1
        return tokens[0]