from sys import stdin, stdout
from math import gcd

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, start, mid)
            self.build(right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, l, r, val, node, start, end):
        if start > end or start > r or end < l:
            return

        if start == end:
            self.tree[node] += val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.update(l, r, val, left_child, start, mid)
            self.update(l, r, val, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def range_sum(self, l, r, node, start, end):
        if start > end or start > r or end < l:
            return 0
        
        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.range_sum(l, r, left_child, start, mid)
        right_sum = self.range_sum(l, r, right_child, mid + 1, end)
        return left_sum + right_sum

def main():
    input = stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    Q = int(data[index])
    index += 1
    
    salaries = list(map(int, data[index:index + N]))
    index += N
    
    happiness = [0] * N
    
    salary_tree = SegmentTree(salaries)
    
    result = []
    
    for _ in range(Q):
        event_type = int(data[index])
        index += 1
        l = int(data[index]) - 1
        index += 1
        r = int(data[index]) - 1
        index += 1
        
        if event_type == 0:
            c = int(data[index])
            index += 1
            for i in range(l, r + 1):
                if salaries[i] != c:
                    if salaries[i] < c:
                        happiness[i] += 1
                    else:
                        happiness[i] -= 1
                salaries[i] = c
        
        elif event_type == 1:
            c = int(data[index])
            index += 1
            
            for i in range(l, r + 1):
                if c > 0:
                    happiness[i] += 1
                elif c < 0:
                    happiness[i] -= 1
                salaries[i] += c
        
        elif event_type == 2:
            total_salary = sum(salaries[l:r + 1])
            count = r - l + 1
            P = total_salary
            Q = count
            divisor = gcd(P, Q)
            result.append(f"{P // divisor}/{Q // divisor}")

        elif event_type == 3:
            total_happiness = sum(happiness[l:r + 1])
            count = r - l + 1
            P = total_happiness
            Q = count
            divisor = gcd(P, Q)
            result.append(f"{P // divisor}/{Q // divisor}")

    stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
