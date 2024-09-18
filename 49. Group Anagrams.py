from collections import defaultdict
from typing import List

print(sorted(["eat", "tea", "tan", "ate", "nat", "bat"]))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            str_ = ''.join(sorted(str))
            map[str_].append(str)
        return list(map.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
