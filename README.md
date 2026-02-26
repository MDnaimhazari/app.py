# app.py
আমাদের আড্ডা
import streamlit as st
import pandas as pd
from datetime import datetime

# ১. অ্যাপের নাম ও কনফিগারেশন
st.set_page_config(page_title="আমাদের আড্ডা", page_icon="💬", layout="centered")

# ডিজাইন কাস্টমাইজেশন
st.markdown("""
    <style>
    .chat-bubble { padding: 10px; border-radius: 15px; margin: 5px; max-width: 70%; }
    .my-msg { background-color: #DCF8C6; align-self: flex-end; }
    .friend-msg { background-color: #FFFFFF; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_index=True)

st.title("💬 আমাদের পার্সোনাল মেসেঞ্জার")

# ২. লগইন লজিক (সহজ জিমেইল ভেরিফিকেশন)
if 'user' not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.subheader("প্রথমে লগইন করুন")
    email = st.text_input("আপনার জিমেইল এড্রেস দিন:")
    if st.button("প্রবেশ করুন"):
        if "@gmail.com" in email:
            st.session_state.user = email
            st.rerun()
        else:
            st.error("দয়া করে সঠিক জিমেইল দিন।")
else:
    # ৩. চ্যাটরুমের মূল অংশ
    st.sidebar.write(f"লগইন আছেন: **{st.session_state.user}**")
    if st.sidebar.button("লগআউট"):
        st.session_state.user = None
        st.rerun()

    # মেসেজ স্টোর করার জন্য ডাটাবেস (সাময়িকভাবে সেশন স্টেট)
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # ৪. মেসেজ ডিসপ্লে
    st.subheader("চ্যাট বক্স")
    for msg in st.session_state.messages:
        div_class = "my-msg" if msg['sender'] == st.session_state.user else "friend-msg"
        st.markdown(f"<div class='chat-bubble {div_class}'><b>{msg['sender']}</b>: {msg['content']} <br><small>{msg['time']}</small></div>", unsafe_allow_index=True)
        
        # যদি ইমেজ থাকে তবে দেখাবে
        if 'image' in msg:
            st.image(msg['image'], width=250)
        if 'video' in msg:
            st.video(msg['video'])

    # ৫. মেসেজ ও ফাইল পাঠানোর ফর্ম
    st.divider()
    with st.form("send_msg", clear_on_submit=True):
        text = st.text_area("মেসেজ লিখুন...", height=100)
        file = st.file_uploader("ছবি বা ভিডিও যোগ করুন", type=['png', 'jpg', 'jpeg', 'mp4'])
        submit = st.form_submit_button("পাঠান 🚀")

        if submit:
            new_msg = {
                "sender": st.session_state.user,
                "content": text,
                "time": datetime.now().strftime("%H:%M"),
            }
            if file:
                if file.type.startswith('image'):
                    new_msg['image'] = file.read()
                elif file.type.startswith('video'):
                    new_msg['video'] = file.read()
            
            st.session_state.messages.append(new_msg)
            st.rerun()
