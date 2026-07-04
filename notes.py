import streamlit as st

st.title("Notes")

if"notes" not in st.session_state:
    st.session_state.notes = []

note =st.text_input("write your note")

if st.button("Add note"):

    st.session_state.notes.append(note)

st.write("MY NOTES:")

for n in st.session_state.notes:
    st.write(n)