import unittest
from sieve import Sieve

class SieveTest(unittest.TestCase):

    def test_sieve_nth_prime(self) -> None:
        sieve = Sieve()
        self.assertEqual(2, sieve.nth_prime(0))
        self.assertEqual(71, sieve.nth_prime(19))
        self.assertEqual(541, sieve.nth_prime(99))
        self.assertEqual(3581, sieve.nth_prime(500))
        self.assertEqual(7793, sieve.nth_prime(986))
        self.assertEqual(17393, sieve.nth_prime(2000))
        self.assertEqual(15485867, sieve.nth_prime(1000000))
        self.assertEqual(179424691, sieve.nth_prime(10000000))
        # self.assertEqual(2038074751, sieve.nth_prime(100000000)) # not required, just a fun challenge

    def test_sieve_fuzz_nth_prime(self) -> None:
        pass