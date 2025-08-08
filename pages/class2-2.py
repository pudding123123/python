import streamlit as st

number = st.number_input("請輸入一個數字", step=1, min_value=60, max_value=70, value=65)

st.write(f"你輸入的數字是: {number}")

import streamlit as st

st.write("練習:成績判斷")
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)
number = int(number)
if number >= 90:
    st.write("A")
elif number <= 89 and number >= 80:
    st.write("B")
elif number <= 79 and number >= 70:
    st.write("C")
elif number <= 69 and number >= 60:
    st.write("D")
else:
    st.write("F")

if st.button("點我", key="button1"):
    st.snow()

if st.button("點我", key="button2"):
    st.balloons()
