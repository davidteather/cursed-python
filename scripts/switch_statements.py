# Formatted
print("Enter 1-5")
key = int(input())-1

arr = ["v=3", "v=5", "print('hahaha')\nv=13", "v=4", "v=19"]
exec(arr[key])
print("V: " + str(v))

# One Liner
exec('''print("Enter 1-5");key = int(input())-1;arr = ["v=3", "v=5", "print('hahaha');v=13", "v=4", "v=19"];exec(arr[key]);print("V: " + str(v))''')