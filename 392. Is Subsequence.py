class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = iter(s)
        s_symbol = next(s)
        for symbol in t:
            if symbol == s_symbol:
                try:
                    s_symbol = next(s)
                except StopIteration:
                    return True
        return False


print(Solution().isSubsequence(s="axc", t="ahbgdc"))
