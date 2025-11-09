import streamlit as st
import random

st.title("🐍 Snake - 💧 Water - 🔫 Gun Game")

choices = {
    "Snake": 1,
    "Water": -1,
    "Gun": 0
}

reverse_choices = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

st.write("Choose one option:")

user_choice = st.selectbox("Your Choice:", ["Snake", "Water", "Gun"])

if st.button("Play"):
    user_val = choices[user_choice]
    computer_val = random.choice([-1, 0, 1])
    computer_choice = reverse_choices[computer_val]

    st.write(f"🤖 **Computer chose:** {computer_choice}")
    st.write(f"🧑 **You chose:** {user_choice}")

    if user_val == computer_val:
        st.info("😐 It's a tie!")
    else:
        # determine winner
        if (computer_val - user_val) == -1 or (computer_val - user_val) == 2:
            st.error("❌ You Lose!")
        else:
            st.success("✅ You Win!")
