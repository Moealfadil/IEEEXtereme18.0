def maximize_number(A, B):
    num_str = list(str(A))
    length = len(num_str)
    max_num = A

    def dfs(depth, swaps_remaining):
        nonlocal max_num
        if swaps_remaining == 0:
            current_num = int("".join(num_str))
            max_num = max(max_num, current_num)
            return

        for x in range(length):
            for y in range(x + 1, length):
                if x == 0 and num_str[y] == '0':
                    continue
                num_str[x], num_str[y] = num_str[y], num_str[x]
                dfs(depth + 1, swaps_remaining - 1)
                num_str[x], num_str[y] = num_str[y], num_str[x]

    dfs(0, B)
    return max_num

A, B = map(int, input().split())
print(maximize_number(A, B))
