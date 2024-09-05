class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        reverse = one_time = False
        lel = s.replace(' ', '').replace('-(', '_').replace('+(', '+')
        print(lel)
        # return sum(map(int, stack))
        pos = 0
        while True:
            if s[pos] + s[pos] == '-(':


print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))
