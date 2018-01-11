# Jay Williams 2017
# This module is included as part of https://github.com/codingJWilliams/jw_utils
# Liscenced according to ../../LISCENCE
# Contact codingJWilliams on github with any queries

import jw_utils

def is_prime(n):
  if n == 0 or n == 1: return False
  for i in range(1, n):
    x = (n - i)
    if x == 0 or x == 1: continue
    if ((n / x) % 1) == 0:
      return False
  return True

def next_prime(n):
  # https://en.wikipedia.org/wiki/Bertrand%27s_postulate
  # There is always a prime number between n and 2n
  for i in range(n * 2):
    x = n + i
    if (x % 2) == 0: continue
    if is_prime(x) and x != n:
      return x
  return "Oh. Well you've proved bertrand wrong. GG"

def primes_between(a, b):
  primesList = []
  currentPrime = a
  while currentPrime < b:
    if is_prime(currentPrime):
      primesList += [currentPrime]
      currentPrime = next_prime(currentPrime)
    else:
      currentPrime = next_prime(currentPrime)
  return primesList