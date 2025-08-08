import streamlit as st

st.write("## 數字金字塔")
number = st.number_input("請輸入數字1~9:", step=1, min_value=1, max_value=9)
st.write("數字金字塔:")
b = 0
for number in range(
    1,
    number + 1,
):
    st.write(str(number) * number)

import streamlit as st

st.write("## 箭頭金字塔")
number = st.number_input("請輸入箭頭的層數1~9:", step=1, min_value=1)
arrow = ""
for a in range(1, number + 1):
    arrow = arrow + (" " * (number - a) + "*" * (a * 2 - 1) + "\n")

for a in range(1, number + 1):
    arrow = arrow + (" " * (number - 1) + "*" + "\n")
st.write(
    f"""
```
{arrow}
```
"""
)
