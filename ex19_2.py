"""
"""
from sys import argv
script, p = argv
p = int(p)

def primetester(p, k):
    return k**(p-1) % p == 1

prime = True

for k in range(p-1):
    if primetester(p, k):
        continue
    else:
        prime = False
        break

print prime
