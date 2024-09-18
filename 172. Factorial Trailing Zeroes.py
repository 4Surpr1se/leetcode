import random


# ./module/func
class Solution:
    def trailingZeroes(self, n: int) -> int:
        counter = 0
        for i in range(4, n + 1):
            while i % 5 == 0:
                counter += 1
                i //= 5
        return counter


for _ in range(1000):
    val = random.randint(1, 10 ** 3)
    res = Solution().trailingZeroes(val)
    fact = 1
    for i in range(1, val + 1):
        fact *= i
        if not str(fact).endswith('0' * res):
            print(res, val, fact)


class Solution:
    def trailingZeroes(self, n):
        x = 5
        res = 0
        while x <= n:
            res = res + n // x
            x = x * 5
        return res
