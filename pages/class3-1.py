print(len([]))
print(len(["蘋果"]))
print(len(["a", "b"]))
print(len([1, 2, 3]))
print("-" * 20)

l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])

print("-" * 20)

for i in l:
    print(i)
print("-" * 20)

l[0] = "A"
l[2] = "c"
print(l)
print("-" * 20)

a = [10, 20, 30]
b = a
b[1] = 200
print(a)
print("-" * 20)

c = [40, 50, 60]
d = c[:]
d[1] = 500
print(c)


l = [1, 2, 3]
l.append(4)
print(l)
print("-" * 20)

l2 = ["a", "b", "c", "b", "a"]
l2.remove("a")
print(l2)
print("-" * 20)

l3 = [1, 2, 3]
l3.pop(1)
print(l3)
print("-" * 20)

l4 = [4, 2, 5, 2, 2, 4]
l4.sort()
print(l4)

l6 = ["蘋果", "香蕉", "橘子"]
l6.sort()
print(l6)
