class Solution(object):
    def reverse(self, x):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        result = 0 #This variable will hold the reverse number of x
        sign = -1 if x < 0 else 1 #Track de x number if is positiv or negativ

        x = abs(x) #Revers de x number

        while x != 0:
            pop = x % 10
            x //= 10

            if result > (INT_MAX - pop) // 10:
                return 0

            result = result * 10 + pop

        return result * sign

solution = Solution()
print(solution.reverse(123))
