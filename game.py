import random
import streamlit as st

# st.title("🪨 Rock-Paper-Scissors ✂️")
st.title("🗿 Rock-Paper-Scissors ✂️")

# Options with emojis
options = {
    # "Rock": "🪨",
    "Rock": "🗿",
    "Paper": "📄",
    "Scissors": "✂️"
}

st.write("Choose your move:")

# Create three buttons with emojis
col1, col2, col3 = st.columns(3)
player_choice = None 

with col1:
    if st.button(options["Rock"], key="rock"):
        player_choice = "Rock"
with col2:
    if st.button(options["Paper"], key="paper"):
        player_choice = "Paper"
with col3:
    if st.button(options["Scissors"], key="scissors"):
        player_choice = "Scissors"

# Play the game if a choice is made
if player_choice:
    computer_choice = random.choice(list(options.keys()))
    
    # Display both choices
    st.markdown(f"### You: {options[player_choice]}    vs    Computer: {options[computer_choice]}")
    
    # Decide winner
    if player_choice == computer_choice:
        st.snow()
        st.success("It's a tie! 🤝")
    elif (
        (player_choice == 'Rock' and computer_choice == 'Scissors') or
        (player_choice == 'Paper' and computer_choice == 'Rock') or
        (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        st.balloons()
        st.success("You win! 🎉")
    else:
        st.error("You lose! 😢")




