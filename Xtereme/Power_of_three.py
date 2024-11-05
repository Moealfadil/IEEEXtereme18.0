import math
try:
    N = int(input())
    log_result = math.log(N, 3)
    x = round(log_result)

    if 3**x == N:
        print(x)
    else:
        print(-1)
except:
    print(-1)
