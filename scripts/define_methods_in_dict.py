# Formatted
print("Enter factorial")
init_val = int(input())
methods = {
    'factorial': "def factorial(x):\n    if x == 1:\n      return 1\n    else:\n      return (x*factorial(x-1))\n\n\nvalue = factorial(init_val)\nprint(value)"
}

exec(methods['factorial'])

# One Liner
exec('''print("Enter factorial")\ninit_val = int(input())\nmethods = {'factorial': "def factorial(x):\\n    if x == 1:\\n      return 1\\n    else:\\n      return (x*factorial(x-1))\\n\\n\\nvalue = factorial(init_val)\\nprint(value)"}\nexec(methods['factorial'])''')