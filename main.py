# Import block
import streamlit as st # UI
import random # Select a random meme
import json # Read the master json file with all the memes

# Page setup
st.set_page_config("Programming Memes", page_icon='🤣', layout='wide')

# Function for getting a meme
def get_a_meme():
    # Get the json data
    with open('memes.json', 'r') as f:
        data = json.load(f)

    # List to hold the paths
    paths = []

    # Extract 'path' from each dictionary in the list
    for item in data:
        paths.append(item['path'])

    # Pick a random path
    url_fragment = random.sample(paths, 1)[0]

    # Add start of url to the picked fragment
    full_url = f"https://raw.githubusercontent.com/deep5050/programming-memes/main/{url_fragment}"
    # import os; os.system(f"open -a \"Google Chrome\" {full_url}")
    
    # Return the random url in full
    return full_url

# Create columns for easier control and visualization (fit content)
col1, col2 =st.columns(2)

# Show the meme display column
with col1:
    found_meme_url = get_a_meme() # Save for the download button
    st.image(found_meme_url)

# Show the page controls column
with col2:
    st.title("Programming Memes")

    st.divider() # Readability on page

    refresh = st.button("🔄 New meme", use_container_width=True) # Button to get a new meme
    if refresh: # The button sets to true when clicked
        pass

    st.markdown("*Right click the image, then click 'Save Image' to download it*")
