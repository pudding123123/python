import random as ra

a = ra.randint(0, 100)
while True:
    b = int(input("請輸入一個數字:"))
    if a > b:
        print("再大一點")

    elif a < b:
        print("再小一點")
    else:
        print("猜中了")
        break
