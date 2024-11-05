import heapq
from collections import defaultdict

def topo_sort(n, m, groups, dependencies):
    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for a, b in dependencies:
        adj_list[a].append(b)
        in_degree[b] += 1

    que = []
    order = []

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(que, (groups[i - 1], i))
    
    while que:
        group_id, project_id = heapq.heappop(que)
        order.append(project_id)
        
        for neighbor in adj_list[project_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(que, (groups[neighbor - 1], neighbor))
    
    return order if len(order) == n else -1

def main():
    n, m = map(int, input().strip().split())
    groups = list(map(int, input().strip().split()))
    dependencies = [tuple(map(int, input().strip().split())) for _ in range(m)]
    
    result = topo_sort(n, m, groups, dependencies)
    
    print("-1" if result == -1 else " ".join(map(str, result)))

if __name__ == "__main__":
    main()
