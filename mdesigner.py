# Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key is not set. Please set it in your environment variables.")

# Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title(':rainbow[Merch AI Designer: Revolutionizing Merchandise Creation]')
st.subheader('I create new merch concepts based on your ideas!')

# Cell 3: Sidebar Title and Design Elements
st.sidebar.title("Make Merch!🧵")
st.sidebar.subheader("Simply complete the form below and tap MAKE IT!")
description_input = st.sidebar.text_area("Describe what you want it to look like🤔:")
merch_type = st.sidebar.selectbox("What kind of merch do you want?",
                                  ("T-Shirt👚", "Album Cover💿", "Mug☕", "Tote Bag👜"))
st.sidebar.write("You selected:", merch_type)
make_it_button = st.sidebar.button('MAKE IT!')

# Cell 4: Function to generate the image
def generate_image(description, merch_type):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return None

    prompt = f"Create a design for a {merch_type} with the following description: {description}"
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Accessing the URL correctly from the response object
    image_url = response.data[0].url
    return image_url

# Handle button click
if make_it_button:
    if description_input.strip() == "":
        st.error("Please provide a description for your merch idea.")
    else:
        thumbnail_url = generate_image(description_input, merch_type)
        if thumbnail_url:
            st.image(thumbnail_url, caption=f'🤩 Your Custom {merch_type} Idea!')
        else:
            st.error("Failed to generate image. Please try again.")