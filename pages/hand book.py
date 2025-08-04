import streamlit as st

st.write(
    """
好的！下面是你今天所學的 Python 指令內容，整理成適合國中生看的筆記，讓你可以更清楚地了解每個指令和它們的用途。

---

## Python 課程筆記 - class1-1.py & class1-2.py

### 1. 基本運算

#### 數學運算

Python 支援許多數學運算，可以用來做加、減、乘、除等運算：

```python
print(7 - 3)  # 減法，結果是 4
print(7 + 3)  # 加法，結果是 10
print(7 * 3)  # 乘法，結果是 21
print(7 / 3)  # 除法，結果是 2.3333...
print(2**3)   # 指數運算，2 的 3 次方，結果是 8
print(7 % 3)  # 取餘數7，除以 3 剩下 1
````

* **`+`**：加法
* **`-`**：減法
* **`*`**：乘法
* **`/`**：除法
* **`**`**：指數運算（例如 2 的 3 次方）
* **`%`**：取餘數

#### 小數運算

Python 也可以處理小數點數字，像是以下的運算：

```python
a = 0.1
b = 0.2
print(a + b)  # 小數相加，結果是 0.3
```

#### 字串處理

字串是由文字組成的資料，可以用來儲存像是名字、句子等資料。你可以用 `+` 把字串連接在一起。

```python
s1 = "hello"
s2 = "world"
s3 = s1 + " " + s2  # 用 + 把兩個字串連接，中間加一個空格
print(s1 + s2)  # 直接顯示 "helloworld"
print(s3)  # 顯示 "hello world"
print(s1 + s2 + s3)  # 顯示 "helloworldhelloworld"
```

如果你想要在字串中插入變數，可以使用 **f-string** 來格式化字串：

```python
name = "Python"
age = 31
a = f"{name} is {age} years old."  # 插入變數進去
print(a)  # 顯示 "Python is 31 years old."
```

#### 字串長度

你可以用 `len()` 來計算字串的長度，也就是字串裡面有多少個字符。

```python
print(len("     "))  # 顯示 5，因為有 5 個空格
print(len(" "))  # 顯示 1，因為有 1 個空格
```

#### 顯示資料型別

Python 中每個資料都有不同的型別，例如數字、字串、布林值等。你可以用 `type()` 來查詢資料的型別。

```python
print(type(""))  # 顯示 <class 'str'>，表示這是一個字串
```

#### 資料類型轉換

有時候你需要把一個資料型別轉換成另一種型別，像是從字串轉換成整數或浮點數：

```python
print(int(False))  # 顯示 0，False 會轉換成 0
print(float(123))  # 顯示 123.0，將整數轉換成浮點數
print(float("123"))  # 顯示 123.0，將字串轉換成浮點數
print(bool("False"))  # 顯示 True，因為非空字串會被視為 True
print(bool(0))  # 顯示 False，0 被視為 False
print(str("True"))  # 顯示 "True"，將布林值 True 轉換成字串
print(str("0.02"))  # 顯示 "0.02"，將浮點數轉換成字串
```

### 2. 使用 `input()` 讓使用者輸入資料

`input()` 函數可以讓程式要求使用者輸入資料，並將輸入的資料儲存在變數中。

```python
print("開始輸入")
a = input("輸入資料:")  # 要求使用者輸入資料
print(a)  # 顯示輸入的資料
print("輸入結束")
print(type(a))  # 顯示資料的型別，因為 input() 會把資料當作字串處理
```

#### 計算圓形面積

你也可以透過 `input()` 輸入數字來計算圓形的面積：

```python
a = int(input("請輸入半徑長度:"))  # 輸入半徑，並轉換為整數
b = 3.14  # 圓周率
c = b * (a**2)  # 計算圓的面積，公式是 pi * r^2
print(c)  # 顯示面積
print(f"圓形的面積是{c}")  # 使用 f-string 格式化輸出
print("圓形的面積是" + str(c))  # 轉換為字串後顯示
print("圓形的面積是", c)  # 用逗號分開顯示字串和數字
```

### 3. 使用 `streamlit` 創建網頁應用

`streamlit` 是一個簡單的 Python 網頁應用程式庫，你可以用它來快速建立網頁介面。

````python
import streamlit as st

st.title("這是標題")  # 顯示標題
st.write("這是write寫的內容")  # 顯示內容
st.text("這是text寫的內容")  # 顯示純文字
st.markdown(
這是用markdown寫的字串
* 文字   **粗體文字**
* *斜體文字*   
* [連結](https://www.example.com)




# 這是標題一

## 這是標題二

### 這是標題三

#### 這是標題四

)

```

- **`st.title()`**：顯示標題
- **`st.write()`**：顯示文字或其他內容
- **`st.text()`**：顯示純文字
- **`st.markdown()`**：顯示格式化的文字，可以使用 Markdown 語法

---

### 小總結

- **數學運算**：`+`, `-`, `*`, `/`, `**`, `%` 等基本運算符號。
- **字串處理**：字串可以用 `+` 連接，還可以格式化顯示變數。
- **資料型別轉換**：使用 `int()`, `float()`, `str()` 等函數轉換資料型別。
- **`input()`**：用來讓使用者輸入資料。
- **`streamlit`**：用來製作簡單的網頁應用。

這些是今天學到的基礎知識，開始練習並創建一些簡單的 Python 程式吧！如果有任何問題，隨時可以問我哦！
"""
)
