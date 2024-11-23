num_days = len(temperatures)
result = num_days * [0]
stack = [] # stores current highest temp that hasn't been overwarmed at bottom
for i, temp in enumerate(temperatures):
    while len(stack) > 0 and temp > stack[-1][1]:
        result[stack[-1][0]] = i - stack[-1][0]
        stack.pop()
    stack.append([i, temp])
return result