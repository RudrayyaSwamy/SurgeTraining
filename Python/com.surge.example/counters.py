#Counters are specialized dictionaries for counting hashable objects. They are part of the collections module.
from collections import Counter

# Create a counter
my_counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])

# Access counts
print(my_counter['apple'])  # Output: 2

# Most common elements
print(my_counter.most_common(1))  # Output: [('banana', 3)]

# Iterate over the counter
for item, count in my_counter.items():
    print(f"{item}: {count}")
