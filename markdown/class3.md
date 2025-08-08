我幫你整理了一份**國中程度也能看懂**的 Python 課堂筆記，把今天所有的程式內容用簡單的方式說明，方便你複習。

---

# 📝 Python 課堂筆記（class 3）

## 1. **列表（List）的操作**

列表就是一種可以裝很多資料的容器，例如：

```python
["蘋果", "香蕉", "橘子"]
```

### 1.1 `len()`：算長度

```python
print(len([]))              # 空列表 → 0
print(len(["蘋果"]))        # 1
print(len([1, 2, 3]))       # 3
```

`len()` 會告訴你列表裡有幾個東西。

---

### 1.2 用 `for` 跑列表

```python
l = [1, 2, 3]
for i in range(len(l)):   # 用索引（位置）
    print(l[i])

for i in l:               # 直接取值
    print(i)
```

---

### 1.3 修改列表的內容

```python
l[0] = "A"    # 把第1個元素改成 "A"
l[2] = "c"
print(l)      # ["A", 2, "c"]
```

---

### 1.4 **複製與影響**

```python
a = [10, 20, 30]
b = a          # b 和 a 是同一個列表
b[1] = 200
print(a)       # a 也被改變

c = [40, 50, 60]
d = c[:]       # d 是 c 的複製品
d[1] = 500
print(c)       # c 不受影響
```

> 記住：直接 `b = a` 會連動，`c[:]` 才是真複製。

---

### 1.5 常用列表方法

```python
l.append(4)       # 在最後加上 4
l.remove("a")     # 刪除第一個 "a"
l.pop(1)          # 刪掉位置1的元素
l.sort()          # 排序（數字或文字）
```

---

## 2. **Streamlit 簡介**（做網頁互動的小工具）

Streamlit 可以讓 Python 做出簡單互動的網頁程式。

### 2.1 欄位（columns）

```python
col1, col2 = st.columns(2)
col1.button("按鈕一")
col2.button("按鈕二")
```

`st.columns()` 可以把畫面分欄，讓按鈕或文字排在不同位置。

---

### 2.2 文字輸入

```python
text = st.text_input("請輸入文字")
st.write(f"你輸入的文字是 {text}")
```

---

### 2.3 Session State（記住資料）

```python
if "var1" not in st.session_state:
    st.session_state.var1 = 1

if st.button("var1+1"):
    st.session_state.var1 += 1
    st.rerun()
```

`st.session_state` 用來記住變數，就算按了按鈕或重新整理也能保留資料。

---

### 2.4 小專案：點餐機

- 使用文字輸入輸入餐點
- 按按鈕加入到「購物籃」
- 刪除功能用 `pop()` 刪掉特定項目

---

## 3. **迴圈控制**

### 3.1 `while` 迴圈

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### 3.2 `break`：提早跳出

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## 4. **隨機數**

```python
import random as ra

ra.randrange(1, 4)     # 產生 1~3（不包含4）
ra.randint(10, 20)     # 產生 10~20（包含20）
```

### 例子：統計隨機數出現次數

```python
count1 = count2 = count3 = 0
for i in range(30):
    a = ra.randrange(1, 4)
    if a == 1:
        count1 += 1
    elif a == 2:
        count2 += 1
    else:
        count3 += 1
```

---

## 5. **猜數字遊戲**

```python
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
```

玩家一直猜，直到答對才結束。

---

## 6. **抽獎模擬**

- 建立空列表 `table`
- 用 `randint()` 抽 1\~100 的號碼
- 用 `not in` 確認號碼沒重複才放進列表
- 計算第幾次抽到 A 賞，以及總花費

---

📌 **今天重點回顧**

1. `len()` 算長度，`for` 跑列表有兩種方法
2. 列表的直接賦值會連動，切片複製才獨立
3. `append()`、`remove()`、`pop()`、`sort()` 是常用操作
4. `while`、`for` 搭配 `break` 控制迴圈
5. `random` 產生隨機數
6. Streamlit 可以做互動網頁，有欄位、文字輸入、按鈕、Session State
7. 小專案：點餐機、猜數字、抽獎模擬

---
