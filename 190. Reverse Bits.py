class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)


print(Solution().reverseBits(43261596))


# я понял
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
