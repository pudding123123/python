# import streamlit as st

# st.title(" 點餐機")
# b, c = st.columns([10, 2])
# a = st.text_input("請輸入餐點")
# if c.button("加入2"):
#     st.write("### 購物籃")
#     st.write(f"{a}")
# r, e = st.columns([10, 2])
# h, d = st.columns([10, 2])
# d.button("刪除", key="1")
# e.button("刪除", key="2")


import streamlit as st

st.title(" 點餐機")

col1, col2 = st.columns([9, 1])
a = col1.text_input("請輸入餐點")
if col2.button("加入", key="add"):
    st.session_state.order.append(a)
    st.rerun()

if "order" not in st.session_state:
    st.session_state.order = []

st.write("### 購物籃")
for i in range(len(st.session_state.order)):
    col3, col4 = st.columns([9, 1])
    col3.write(st.session_state.order[i])
    if col4.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
