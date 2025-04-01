package sieve

import (
	"math"
)

// this defines an interface for finding the Nth prime number.
type Sieve interface {
	NthPrime(n int64) int64
}

// sieveImpl is the actual implementation of the Sieve interface that we defined above.
type sieveImpl struct{}

// this returns a new instance that implements the Sieve interface.
func NewSieve() Sieve {
	return &sieveImpl{}
}

// finds the Nth prime number (0-based index).
func (s *sieveImpl) NthPrime(n int64) int64 {
	if n < 0 {
		panic("n must be non-negative")
	}
	if n == 0 {
		return 2
	}

	// upper_bound = n * (log(n) + log(log(n)))
	// A small margin is added
	// to ensure we include the required prime.
	estimateUpperBound := func(n int64) int64 {
		if n < 6 {
			return 13
		}
		nf := float64(n)
		upper := nf * (math.Log(nf) + math.Log(math.Log(nf)))
		return int64(upper) + 10
	}

	// Get an initial estimate of the upper bound.
	upperBound := estimateUpperBound(n)

	var primes []int64
	for {
		// composite or not
		isComposite := make([]bool, upperBound+1)
		isComposite[0], isComposite[1] = true, true // 0, 1

		// Running Sieve of Eratosthenes algorithm.
		for i := int64(2); i*i <= upperBound; i++ {
			if !isComposite[i] {
				for j := i * i; j <= upperBound; j += i {
					isComposite[j] = true
				}
			}
		}

		// Collect all the primes found.
		primes = nil
		for i := int64(2); i <= upperBound; i++ {
			if !isComposite[i] {
				primes = append(primes, i)
			}
		}

		// Once we have found at least (n+1) primes, we're done.
		if int64(len(primes)) > n {
			break
		}

		//else, increase the upper_bound and try again.
		upperBound = estimateUpperBound(upperBound * 2)
	}

	return primes[n]
}
