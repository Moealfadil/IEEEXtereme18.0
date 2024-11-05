#include <stdio.h>
A, B = map(int, input().split())
C = list(map(int, input().split()))

D = [False] * (A + 1)

for c in C:
    if c <= A:
        for i in range(c, A + 1, c):
            D[i] = True

print(sum(D))