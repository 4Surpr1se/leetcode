from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_ = Counter(s)
        for symbol in t:
            t_symbol = dict_[symbol] = dict_[symbol] - 1
            if t_symbol < 0:
                return False
        return dict_.total() == 0


print(Solution().isAnagram('sds', 'ds'))
