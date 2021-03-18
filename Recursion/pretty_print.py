# Pretty print a dictionary structure
# Input: A dictionary and a string
# Output:
# Purpose: Pretty print a dictionary structure

def pretty_print(dictionary, indent=""):
    # iterate through every key in the dictionary
    for key in dictionary:
        # get the value associated with the key
        val = dictionary[key]
        # check the type of the key to see if it's another dict
        if isinstance(val, dict):
            print(f"{indent}{key}:")
            pretty_print(dictionary[key], indent + "  ")
        else:
          # it's the val isn't a dict then just print out they key and val
            print(f"{indent}{key}: {val}")


o1 = {"a": 1, "b": 2}

print(pretty_print(o1))
