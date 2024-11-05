def arrange_bricks(N, x, A):
    A.sort(reverse=True)
    stacks = []

    for brick in A:
        placed = False
        for stack in stacks:
            if brick + x <= stack[-1]:
                stack.append(brick)
                placed = True
                break
        if not placed:
            stacks.append([brick])
    
    print(len(stacks))
    for stack in stacks:
        print(len(stack), ' '.join(map(str, stack)))

if __name__ == "__main__":
    first_line = input()
    N, x = map(int, first_line.split())
    second_line = input()
    A = list(map(int, second_line.split()))
    arrange_bricks(N, x, A)
