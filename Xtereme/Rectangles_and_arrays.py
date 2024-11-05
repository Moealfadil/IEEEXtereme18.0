def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Append a height of 0 to flush out the stack at the end
    
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
    
    return max_area

def maxRectangleWithModification(N, X, A):
    # Step 1: Calculate the maximum area without modification
    max_area = largestRectangleArea(A[:])
    
    # Step 2: Calculate potential max area with modification
    for i in range(N):
        if A[i] < X:  # Only modify if it's beneficial
            original_height = A[i]
            A[i] = X
            
            # Calculate area with this modification
            modified_area = largestRectangleArea(A)
            max_area = max(max_area, modified_area)
            
            # Restore the original height
            A[i] = original_height
    
    return max_area

# Input reading
N, X = map(int, input().split())
A = list(map(int, input().split()))

# Calculate and print the result
result = maxRectangleWithModification(N, X, A)
print(result)
