class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all(s[i] == s[~i] for i in range(len(s) // 2))
