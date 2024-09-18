from collections import Counter, defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ALPHABET_LEN = 1000
        s_range = (f'.{h}.' for h in range(0, ALPHABET_LEN))
        s_map = {}
        t_range = (f'.{le}.' for le in range(0, ALPHABET_LEN))
        t_map = {}
        for symbol in s:
            s = s.replace(symbol, s_map.get(symbol, next(s_range)))
        for symbol in t:
            t = t.replace(symbol, t_map.get(symbol, next(t_range)))
        print(s, t)
        return s == t


print(Solution().isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"))
