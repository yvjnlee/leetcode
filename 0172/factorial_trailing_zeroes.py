class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        factorial = 1

        for i in range(1, n+1):
            factorial *= i

        while factorial % 10 == 0:
            res += 1
            factorial = factorial // 10

        return res
