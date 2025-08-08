這裡是根據你今天上課學到的內容，整理出來的一份**適合國中生閱讀的 Python 筆記**，使用簡單易懂的語言來說明每一個觀念和指令：

---

# 🐍 Python 程式設計課筆記：第二堂課

## 一、比較運算子（用來比較兩個東西）

```python
print(1 == 1)   # 是否相等？ True
print(1 != 1)   # 是否不相等？ False
print(1 >= 2)   # 是否大於等於？ False
print(1 <= 2)   # 是否小於等於？ True
print(1 > 2)    # 是否大於？ False
print(1 < 2)    # 是否小於？ True
```

---

## 二、邏輯運算子（用來組合條件）

```python
print(not True)       # not 是「不是」的意思 → False
print(True and False) # and 是「而且」的意思 → False
print(True or False)  # or 是「或者」的意思 → True
```

| 運算子 | 中文意思 | 範例                   |
| ------ | -------- | ---------------------- |
| `not`  | 不是     | not True → False       |
| `and`  | 而且     | True and False → False |
| `or`   | 或者     | True or False → True   |

---

## 三、密碼驗證練習

```python
password = input("請輸入密碼:")
if password == "1234":
    print("密碼正確，Josh歡迎回家!")
elif password == "5678":
    print("密碼正確，Dino歡迎回家!")
else:
    print("密碼錯誤")
```

✅ 用 `if` 判斷條件，`elif` 表示「如果不是上一個條件，試試看這個」，`else` 是「以上都不是」。

---

## 四、閏年判斷（進階練習）

### 方法一：

```python
year = int(input("請輸入年份:"))
if year % 400 == 0:
    print("是閏年")
elif year % 100 == 0:
    print("不是閏年")
elif year % 4 == 0:
    print("是閏年")
else:
    print("不是閏年")
```

### 方法二（巢狀 if）：

```python
year = int(input("請輸入年份:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("是閏年")
        else:
            print("不是閏年")
    else:
        print("是閏年")
else:
    print("不是閏年")
```

---

## 五、Streamlit 基礎（做出互動介面的小工具）

### 範例 1：輸入一個數字

```python
import streamlit as st
number = st.number_input("請輸入一個數字", step=1, min_value=60, max_value=70, value=65)
st.write(f"你輸入的數字是: {number}")
```

### 範例 2：成績判斷

```python
number = st.number_input("請輸入成績", step=1, min_value=0, max_value=100)
if number >= 90:
    st.write("A")
elif number >= 80:
    st.write("B")
elif number >= 70:
    st.write("C")
elif number >= 60:
    st.write("D")
else:
    st.write("F")
```

### 加上一點特效：

```python
if st.button("點我", key="button1"):
    st.snow()       # 下雪效果
if st.button("點我", key="button2"):
    st.balloons()   # 氣球飛起來
```

---

## 六、for 迴圈（重複做事情）

```python
for i in range(10):
    print(i)  # 從0~9

for a in range(2, 6):
    print(a)  # 從2~5

for b in range(2, 10, 2):
    print(b)  # 從2開始，每次+2，到9
```

---

## 七、金字塔練習（搭配 Streamlit）

### 數字金字塔

```python
number = st.number_input("請輸入數字1~9", step=1, min_value=1, max_value=9)
for i in range(1, number + 1):
    st.write(str(i) * i)
```

### 星星箭頭金字塔

````python
arrow = ""
for i in range(1, number + 1):
    arrow += " " * (number - i) + "*" * (i * 2 - 1) + "\n"
for i in range(1, number + 1):
    arrow += " " * (number - 1) + "*" + "\n"
st.write(f"```\n{arrow}\n```")
````

---

## 八、List（串列）資料結構

List 是一種可以裝很多東西的資料型別。

```python
L1 = []                            # 空的串列
L2 = ["蘋果"]                     # 一個水果
L3 = ["蘋果", "香蕉", "橘子"]     # 三個水果
L4 = [1, 2, 3, 4, 5]               # 數字串列
L5 = [1, "蘋果", True, 3.14]       # 不同型別混合
L6 = [1, 2, 3, ["蘋果", "香蕉"]]  # 串列裡面還可以有串列
```

### 如何取出東西？

```python
print(L6[1])       # 第二個元素 → 2
print(L6[3][0])    # 第四個元素裡的第一個 → "蘋果"
```

### 切割串列

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[1:4:2])   # 從第2個開始，到第4個之前，每隔一個 → [2, "a"]
print(L[1:4])     # 從第2到第4（不含第5）→ [2, 3, "a"]
print(L[::2])     # 每隔一個 → [1, 3, "b"]
```

---

## ✅ 小結

你今天學到的技能包含：

- 如何比大小和判斷相等
- 邏輯判斷（and, or, not）
- if 條件判斷式
- 使用 Streamlit 做互動介面
- 用 for 迴圈重複做事情
- 金字塔練習（文字藝術）
- 串列 List 的基本用法
