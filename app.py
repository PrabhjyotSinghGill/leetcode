class Solution:
    def reverse(self, x: int) -> int:
        abs_value = abs(x)
        sign = 1 if x >= 0 else -1 
        reverse = 0
        max_value = 2 ** 31 - 1
        while abs_value > 0:
            reverse = reverse * 10 + (abs_value % 10)
            abs_value //= 10
            if reverse > max_value:
                return 0
        return reverse * sign
