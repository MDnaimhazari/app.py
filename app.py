import streamlit as st

st.set_page_config(page_title="নাহিদের মেসেঞ্জার", page_icon="💬")
st.title("💬 নাহিদের ব্যক্তিগত মেসেঞ্জার")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("আপনার মেসেজ এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = f"আপনি বলেছেন: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
