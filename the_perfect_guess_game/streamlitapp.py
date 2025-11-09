import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "guess_count" not in st.session_state:
    st.session_state.guess_count = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.write("I have selected a number between **1 and 100**. Try to guess it!")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Submit guess button
if st.button("Submit Guess"):
    if st.session_state.game_over:
        st.warning("Game is already over! Click Restart to play again.")
    else:
        st.session_state.guess_count += 1

        if guess > st.session_state.number:
            st.info("🔽 Enter a **lower** number!")
        elif guess < st.session_state.number:
            st.info("🔼 Enter a **higher** number!")
        else:
            st.success(
                f"🎉 Correct! The number was **{st.session_state.number}**.\n\n"
                f"You guessed it in **{st.session_state.guess_count} attempts**."
            )
            st.session_state.game_over = True

# Restart button
if st.button("Restart Game"):
    st.session_state.numb_

