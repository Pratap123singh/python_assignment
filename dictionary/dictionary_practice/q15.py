#15. Write a Python program to get the maximum and minimum values of a dictionary.
d1={1:10, -2:20, 3:30, -4:40}

print("Max value: ", max(d1.values()))
print("Min value: ", min(d1.values()))

print("Max key: ", max(d1.keys()))
print("Min key: ", min(d1.keys()))