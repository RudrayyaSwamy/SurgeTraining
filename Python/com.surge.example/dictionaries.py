#Dictionaries are unordered collections of key-value pairs. Keys must be unique and immutable, but values can be of any type and can be duplicated.
# Create a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Access values by key
print(my_dict['name'])  # Output: Alice

# Add a new key-value pair
my_dict['email'] = 'alice@example.com'

# Remove a key-value pair
del my_dict['age']

# Iterate over keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
