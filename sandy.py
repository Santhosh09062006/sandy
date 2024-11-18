import streamlit as st

port=st.button("portfolio")
if port:
   st.title("PORTFOLIO for santhosh kumar G")
   st.subheader("technical skills : python,html and cs")
   st.subheader("electronic communication concepts:semiconductor circuits")

st.title("binary search number guessing game")

st.write("think of a number between 1 and 100, and i will try to guess it !")
st.write("you will tell me if my guess is too high,too low or correct.")
 
 if 'low'not in st.session_state:
    st.session_state.low=1
    st.ession_state.high=100
    st.session_state.guess=(st.session_state.low+st.session_state.high)//2
    st.session_state.attempts=0

st.write(f"my current guess is:**{st.session_state}**")

col1,col2,col3=st.columns(3)

with col1:
    if st.button("too low"):
        st.session_state.low=st.session_state.guess+1
        st.session_state.attempts+=1

with col2:
    if st.button("too high"):
        st.session_state=st.session_state.guess-1
        st.session_state.attempts+=1

with col3:
    if st.button("correct!"):
        st.success(f"i guessed your number**{st.session_state.guess}**{st.session_state.attempts}attempts!")
        st.session_state.low=1
        st.session_state.high=100
        st.session_state.attempts=0

if st.session_state.low<=st.session_state.high:
    st.session_state.guess=(st.session_state.low+st.session_state.high)//2

else:
    st.error("it seems like there was a mistake. please restart the game.")

if st.button("reset game"):
    st.session_state.low=1
    st.session_state.high=100
    st.session_state.guess=(st.session_state.low+st.session_state.high)//2
    st.session_state.attempts=0
    st.success("game has been reset!start thinking of a new number.")