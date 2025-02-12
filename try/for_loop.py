# This code calculates the total number of iterations in a nested loop structure.               
# The outer loop runs 100 times, the middle loop runs 100 times for each iteration of the outer loop,
# and the innermost loop runs 100 times for each iteration of the middle loop.
# Therefore, the total number of iterations is 100 * 100 * 100 = 1,000,000.
# The variable 'h' is incremented by 1 in each iteration, so it will be 1,000,000 at the end.
h = 0
for i in range(100):
    h = h + 1
    for j in range(100):
        h = h + 1
        for k in range(100):
            h = h + 1

print(h)