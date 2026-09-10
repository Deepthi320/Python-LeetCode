class Solution:

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        while x != 0:
            digit = x % 10
            x //= 10

            if reversed_num > (MAX_INT - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        result = sign * reversed_num
        if result < MIN_INT or result > MAX_INT:
            return 0

        return result
