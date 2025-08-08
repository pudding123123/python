import random as ra

table = []
a = int(input("請輸入你所選擇的A賞編號(1~100):"))
for i in range(100):
    b = ra.randint(1, 100)
    if b not in table:
        table.append(b)
        table.sort()

c = len(table)
print(table)
print(c)
count = 0
for a in range(100):
    count += 1
    if a == b:
        num = int(count) * 200
        print(f"你在第{count}抽抽到A賞，總共花費200*{count}={num}元")
