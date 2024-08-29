#Deques are double-ended queues that allow appending and popping from both ends. They are part of the collections module.
from collections import deque

# Create a deque
my_deque = deque([1, 2, 3, 4, 5])

# Append elements
my_deque.append(6)
my_deque.appendleft(0)

# Pop elements
my_deque.pop()       # Removes 6 from the end
my_deque.popleft()  # Removes 0 from the beginning

# Iterate over the deque
for item in my_deque:
    print(item)
