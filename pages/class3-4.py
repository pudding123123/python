i = 0
while i < 5:
    print(i)
    i += 1
print("-" * 20)

i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
print("-" * 20)

for i in range(5):
    if i == 3:
        break
    print(i)


print("-" * 20)

import random as ra

count1 = 0
count2 = 0
count3 = 0
for i in range(30):
    a = ra.randrange(1, 4)  # 產生1~3的隨機數字
    if a == 1:
        count1 += 1
    elif a == 2:
        count2 += 1
    else:
        count3 += 1
    print(a)
    print(count1, count2, count3)

print("-" * 20)

print(ra.randrange(0, 10, 2))
print(ra.randint(10, 20))  # 有包含終止數
