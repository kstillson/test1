#!/usr/bin/env python3
"""Calculate factorials.  v2 """

import argparse


def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError('factorial is undefined for negative numbers')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    ap = argparse.ArgumentParser(description='Calculate n!')
    ap.add_argument('n', type=int, nargs='+', help='non-negative integer(s)')
    args = ap.parse_args()
    for n in args.n:
        print(f'{n}! = {factorial(n)}')


if __name__ == '__main__':
    main()
