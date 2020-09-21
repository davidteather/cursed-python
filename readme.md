# Cursed Python

I discovered the wonders of exec and decided to find more cursed python fuctionality.

## Switch Statements

Use an array to run the code of the switch statement and the index is what the value equals.
```
print("Enter 1-5")
key = int(input())-1

arr = ["v=3", "v=5", "print('hahaha')\nv=13", "v=4", "v=19"]
exec(arr[key])
print("V: " + str(v))

```

One Liner
```
exec('''print("Enter 1-5");key = int(input())-1;arr = ["v=3", "v=5", "print('hahaha');v=13", "v=4", "v=19"];exec(arr[key]);print("V: " + str(v))''')
```

## Define Methods in Dictionaries

Defines a method with parameters within a dictionary
```
print("Enter factorial")
init_val = int(input())
methods = {
    'factorial': "def factorial(x):\n    if x == 1:\n      return 1\n    else:\n      return (x*factorial(x-1))\n\n\nvalue = factorial(init_val)\nprint(value)"
}

exec(methods['factorial'])
```

One Liner
```
exec('''print("Enter factorial")\ninit_val = int(input())\nmethods = {'factorial': "def factorial(x):\\n    if x == 1:\\n      return 1\\n    else:\\n      return (x*factorial(x-1))\\n\\n\\nvalue = factorial(init_val)\\nprint(value)"}\nexec(methods['factorial'])''')
```