a=10
b=10
print(id(a))
print(id(b))

print(a is not b)

a=5
print(id(a))
a=8
print(id(a))

print(a is a)

a = 10
b = 10
print(a is b)   # ✅ True → Python reuses small numbers (−5 to 256)

x = 1000
y = 1000
print(x is y)   # ❌ Might be False → Python may create new object

list1 = [1, 2]
list2 = [1, 2]
print(list1 == list2)  # ✅ True → same value
print(list1 is list2)  # ❌ False → different objects
