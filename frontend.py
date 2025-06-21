import streamlit as st
import httpx

st.title("Mood-Based Playlist Generator")

# User enters their mood
user_input = st.text_input("Describe your mood:")

# Add a slider to control playlist length (min 1, max 30)
num_songs = st.slider("How many songs?", min_value=1, max_value=30, value=10)

if st.button("Get Playlist") and user_input:
    # Send request to FastAPI backend
    with httpx.Client() as client:
        response = client.get(
            "http://localhost:8000/playlist/",
            params={"user_input": user_input, "limit": num_songs}
        )
    if response.status_code == 200:
        data = response.json()
        st.write(f"**Detected mood:** {data['mood']}")
        st.write("### Your Playlist:")
        for song in data["playlist"]:
            st.write(f"- **{song['title']}** by *{song['artist']}*")
    else:
        st.error("Could not get a playlist. Is your FastAPI server running?")
