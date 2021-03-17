# Solutions

### Fibonacci Solution

```python
def fib(n):
    if n < 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

### Reverse String Solution

```python
def reverse(ss):
    if len(ss) == 0:
        return ""
    return ss[-1] + reverse(ss[:-1])
```

### Pretty Print Solution

```python
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
```
