from math import log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # количество цифр в числе пропорционально логарифму числа
        # http://ipo.spb.ru/iumk/Math_XXI//Labs/Lab_2.3.3-1/Lab_2.3.3-1.html
        num_length = int(log10(x)) + 1
        while num_length > 0:
            end = x % 10
            len_rn = 10 ** (num_length - 1)
            start = x // len_rn
            if end != start:
                return False
            x = (x % len_rn) // 10
            num_length -= 2
        return True


# я не уверен, что это лучше, оно точно проще, но он в любом случае будет переворачивать число полностью
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x
