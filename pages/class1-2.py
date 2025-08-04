import streamlit as st

st.title("這是標題")
st.write("這是write寫的內容")
st.text("這是text寫的內容")
st.markdown(
    """
這是用markdown寫的字串
* 文字   **粗體文字**
* *斜體文字*   
* [連結](https://www.example.com)
```python
print("Hello, World!")
```
# 這是標題一
## 這是標題二
### 這是標題三
#### 這是標題四
"""
)
