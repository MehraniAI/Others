#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("growth mindset challenge:web app with streamlit")
st.header("🚀welcome to your growth journey!")
st.write("a growth journey is a continuous process of self-discovery, improvement, and learning, encompassing personal and professional development, aiming to unlock one's full potential and achieve a more fulfilling life.")
#quotes section
st.header("💡today's growth minset quotes")
st.write("🔥It is hard to fail but it is worse never to have tried to succeed.🌝")
st.header("📌what's your challenge today")
user_input = st.text_input("describe a challenge you're facing:")
#condition
if user_input:
    st.success(f"🙌you're facing:{user_input}.keep pushing forward towards your goal!⌛")
else:
    st.warning("tell us your chalenge to get started!")
#reflexing
st.header ("🧠reflect on your learning")
reflection = st.text_area("write your outcome here:")
if reflection:
    st.success(f"✨Great insight! your reflection:{reflection}")
else:
    st.info("reflecting on past experience help you grow! share your diffculties")
#achivements 
st.header("🎉celebrate your wins🏅!")
acheivment= st.text_input("share something you've recently accomplished:")
if acheivment:
    st.success(f"Amazing! you achived:{acheivment}")
else:
    st.info("big or small ,every acheivement counts!share one now!" )
#footer
st.write("- - -")
st.write("❤️️keep believing in yourself. growth is a journey, not a destination!😎")
st.write("📰created by tehreem fatima♊️***")