
import streamlit as st

# পেজ সেটআপ ও ইমোজি
st.set_page_config(page_title="নাহিদের মেসেঞ্জার", page_icon="💬")

# সুন্দর হেডিং
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>💬 নাহিদের ব্যক্তিগত মেসেঞ্জার 🔥</h1>", unsafe_allow_html=True)
st.write("---")

# চ্যাট হিস্টোরি রাখার জন্য
if "messages" not in st.session_state:
    st.session_state.messages = []

# আগের মেসেজগুলো দেখানোর জন্য
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার মেসেজ লিখলে যা হবে
if prompt := st.chat_input("এখান থেকে ইমোজি পাঠান... 😊🚀🔥"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"{prompt} 😎")
    
    # অটো রিপ্লাই
    response = f"আপনার মেসেজটি নাহিদ পেয়েছে! ধন্যবাদ। ✨🙏"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
