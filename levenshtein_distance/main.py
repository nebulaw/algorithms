#!/usr/bin/env python3

import functools

# simple version of levenshtein distance
def levsimple(s1, s2):
    if len(s1) == 0: return len(s2)
    if len(s2) == 0: return len(s1)
    if s1[-1] == s2[-1]: return levsimple(s1[:-1], s2[:-1])
    return 1 + min(
        levsimple(s1[:-1], s2),
        levsimple(s1, s2[:-1]),
        levsimple(s1[:-1], s2[:-1]))

# using cache
@functools.cache
def levn_aux(s1, s2, n1, n2):
    if n1 == 0: return n2
    if n2 == 0: return n1
    if s1[n1-1] == s2[n2-1]: return levn_aux(s1, s2, n1-1, n2-1) # ignore
    return 1 + min(
        levn_aux(s1, s2, n1-1, n2),    # remove
        levn_aux(s1, s2, n1, n2-1),    # foo
        levn_aux(s1, s2, n1-1, n2-1))  # replace

def levn(s1, s2): return levn_aux(s1, s2, len(s1), len(s2))

def trace_cache(cache):
    for row in cache:
        for item in row: print("-" if item is None else item, end=" ")
        print()
    print()

def levcache_aux(s1, s2, n1, n2, cache):
    if cache[n1][n2] is not None: return cache[n1][n2]
    if n1 == 0:
        cache[n1][n2] = n2
        return cache[n1][n2]
    if n2 == 0:
        cache[n1][n2] = n1
        return cache[n1][n2]
    if s1[n1-1] == s2[n2-1]:
        cache[n1][n2] = levcache_aux(s1, s2, n1-1, n2-1, cache)
        return cache[n1][n2]
    cache[n1][n2] = 1 + min(
        levcache_aux(s1, s2, n1-1, n2, cache),
        levcache_aux(s1, s2, n1, n2-1, cache),
        levcache_aux(s1, s2, n1-1, n2-1, cache))
    return cache[n1][n2]

def levcache(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    cache_data = []
    for _ in range(n1 + 1): cache_data.append([None] * (n2 + 1))
    return levcache_aux(s1, s2, len(s1), len(s2), cache_data)

