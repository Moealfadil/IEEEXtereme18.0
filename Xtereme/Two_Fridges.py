import sys
input = sys.stdin.read
def find_fridge_temperatures(n, intervals):
    if n == 0:
        return -1

    min_a = min(interval[0] for interval in intervals)
    max_b = max(interval[1] for interval in intervals)

    for T1 in range(-100, 101):
        for T2 in range(T1, 101):
            if all((a <= T1 <= b or a <= T2 <= b) for a, b in intervals):
                return T1, T2

    return -1

if __name__ == "__main__":
    try:
        user_input = input()
        data = user_input.split()
        
        n = int(data[0])
        intervals = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(n)]
    except (IndexError, ValueError):
        print(-1)
        sys.exit(1)
    
    result = find_fridge_temperatures(n, intervals)
    if result == -1:
        print(-1)
    else:
        print(result[0], result[1])