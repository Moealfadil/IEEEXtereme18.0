def dfs(city, graph, stars, visited, current_count, last_star):
    visited[city] = True
    max_count = current_count

    if stars[city] > last_star:
        current_count += 1
        last_star = stars[city]

    max_count = max(max_count, current_count)

    for neighbor in graph[city]:
        if not visited[neighbor]:
            max_count = max(max_count, dfs(neighbor, graph, stars, visited, current_count, last_star))

    visited[city] = False
    return max_count

def max_cities_visited():
    n = int(input())
    stars = list(map(int, input().split()))
    graph = {i: [] for i in range(n)}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    start_city = stars.index(min(stars))
    visited = [False] * n
    max_cities = dfs(start_city, graph, stars, visited, 0, -1)
    print(max_cities)

max_cities_visited()
