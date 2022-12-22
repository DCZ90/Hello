s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(5)

print(s)

#Remove and existing value
s.remove(5)
print(s)

print("The set has: " + str(len(s)) + " elements")
print(f"The set has: {len(s)} elements.")