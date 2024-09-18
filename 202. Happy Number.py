class Solution:
    def isHappy(self, n: int) -> bool:
        has_been = []
        # https://pythonz.net/references/named/slozhnost-operatsii-so-slovaryami/
        while n not in has_been:
            has_been.append(n)
            n = sum(map(lambda x: int(x) ** 2, str(n)))
            if n == 1:
                return True
        return False