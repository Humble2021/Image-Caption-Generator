import streamlit as st
import os
from PIL import Image
import requests
from io import BytesIO
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GENAI_API_KEY"))  # Replace GENAI_API_KEY with your actual API key
image_model = genai.GenerativeModel("gemini-pro-vision")

def get_caption(platform, max_length, image):
    min_length = 20
    if platform is None:
        text = f"Generate a caption for this image: {image} with a max length of {max_length} and min length of {min_length}."
    else:
        text = f"Generate me a caption for this image for {platform}: {image}. which i can use on my {platform} and the caption should be of max length {max_length} and min length of {min_length}"
    response = image_model.generate_content([text, image])
    
    if response.candidates:
        candidate = response.candidates[0]
        if candidate.safety_ratings:
            # Check if the response contains parts
            if candidate.content and candidate.content.parts:
                # Extract the text from the content parts
                return candidate.content.parts[0].text
    
    return "Caption generation failed or response was blocked."


def generate_caption_from_image(image, platform, max_length):
    try:
        caption = get_caption(platform, max_length, image)
        return caption
    except Exception as e:
        return f"Error occurred: {str(e)}"

st.title("Image Caption Generator")
st.write("This app generates a caption for an image.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
max_length = st.slider("Select length of the caption", 50, 100, 70)

platform = ""
if st.button("Identify image"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Generating caption...")
        caption = generate_caption_from_image(image, platform, max_length)
        st.write(f"Caption: {caption}")
    else:
        st.write("Please upload an image file.")

if st.button("Insta Caption"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Generating caption for Instagram...")

        # Convert image to bytes
        img_byte_array = BytesIO()
        image.save(img_byte_array, format=image.format)
        img_byte_array = img_byte_array.getvalue()

        # Prepare payload
        payload = {
            "contents": [{"parts": [{"text": "Describe the image"}]}]
        }

        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('GENAI_API_KEY')}"
        }

        # Make POST request to Google Generative AI API
        response = requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent", headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            print(data)
            caption = data['contents'][0]['parts'][0]['text']
            st.write(f"Caption: {caption}")
        else:
            st.write("Failed to generate caption.")
    else:
        st.write("Please upload an image file.")
