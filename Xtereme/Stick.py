def union_area_of_squares(N, K, L):
    events = []
    for i in range(N):
        x_start = i * K - L
        x_end = i * K + L
        y_bottom = i * K - L
        y_top = i * K + L
        events.append((x_start, y_bottom, y_top, 1))
        events.append((x_end, y_bottom, y_top, -1))

    events.sort()
    
    active_intervals = []
    previous_x = events[0][0]
    total_area = 0
    
    def calculate_y_coverage():
        if not active_intervals:
            return 0
        active_intervals.sort()
        current_start, current_end = active_intervals[0]
        y_coverage = 0
        for start, end in active_intervals:
            if start > current_end:
                y_coverage += current_end - current_start
                current_start, current_end = start, end
            else:
                current_end = max(current_end, end)
        y_coverage += current_end - current_start
        return y_coverage
    
    for x, y_bottom, y_top, event_type in events:
        total_area += (x - previous_x) * calculate_y_coverage()
        previous_x = x
        
        if event_type == 1:
            active_intervals.append((y_bottom, y_top))
        else:
            active_intervals.remove((y_bottom, y_top))
    
    return total_area

N, K, L = map(int, input().split())
print(union_area_of_squares(N, K, L))
