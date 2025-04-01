import math

class Sieve:
    def __init__(self) -> None:
        pass
    def nth_prime(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be a non-negative integer.")
        if n == 0:
            return 2

        upper_bound = self.estimate_upper_bound(n)
        
        primes = self.sieve_of_eratosthenes(upper_bound)

        while len(primes) <= n:
            upper_bound *= 2
            primes = self.sieve_of_eratosthenes(upper_bound)

        return primes[n]

    def estimate_upper_bound(self, n: int) -> int:
        if n < 6:
            return 13  # A small upper bound for small n
        n = float(n)
        return int(n * (math.log(n) + math.log(math.log(n)))) + 1

    def sieve_of_eratosthenes(self, limit: int) -> list:
        is_prime = [True] * (limit + 1)
        p = 2
        while (p * p <= limit):
            if is_prime[p]:
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, limit + 1) if is_prime[p]]
        return primes