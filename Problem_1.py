# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Complexity:
# Time O(n*m), where m is the number of primes
# Space O(n)

# Note: There is a time/space O(1) solution for the case of 3 and 5 using the inclusion-exclusion formula, but it doesn't generalize efficiently to an arbitrary number of prime multiples.

class Solution:
    def get(self, primes: list, n: int) -> int:
        multiples = set()
        for prime in primes:
            multiple = prime
            while multiple < n:
                multiples.add(multiple)
                multiple += prime
        return sum(multiples)

solution = Solution()
print(solution.get([3, 5], 1000))