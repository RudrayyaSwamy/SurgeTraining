#Named tuples are like regular tuples but with named fields that you can access as attributes.
from collections import namedtuple

# Define a named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an instance
p = Person(name='Bob', age=25, city='Los Angeles')

# Access fields
print(p.name)  # Output: Bob

# Iterate over the fields
for field in p._fields:
    print(f"{field}: {getattr(p, field)}")
