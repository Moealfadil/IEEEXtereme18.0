def queris_prog(N, Q, P, queries):
    A = [0] * (N + 1)
    output = []

    for query in queries:
        if query[0] == 0:
            _, l, r, c = query
            for i in range(l, r + 1):
                A[i] += c
        elif query[0] == 1:
            _, l, r, c = query
            for i in range(l, r + 1):
                A[P[i - 1]] += c
        elif query[0] == 2:
            _, l, r = query
            total_sum = sum(A[l:r + 1])
            output.append(total_sum)
        elif query[0] == 3:
            _, l, r = query
            total_sum = sum(A[P[i - 1]] for i in range(l, r + 1))
            output.append(total_sum)

    return output

if __name__ == "__main__":
    N, Q = map(int, input().split())
    P = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)

    results = queris_prog(N, Q, P, queries)
    for res in results:
        print(res)
