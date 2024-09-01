from io import BytesIO
import streamlit as st
from PIL import Image
from rembg import remove

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.markdown("""
    <style>
        h1 {
            color: #dc3545;
            font-size: 2.5em;
            text-align: center;
        }
        .description {
            color: #343a40;
            font-size: 1em;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-size: 1.1em;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            transition: background-color 0.3s ease, transform 0.2s;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Background Remover</h1>", unsafe_allow_html=True)

st.markdown('<p class="description">Upload and process your image.</p>', unsafe_allow_html=True)

st.sidebar.header("Actions")

col1, col2 = st.columns(2)

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def process_image(upload):
    image = Image.open(upload)
    col1.image(image, caption="Original", use_column_width=True)

    processed_image = remove(image)
    col2.image(processed_image, caption="Processed", use_column_width=True)

    st.sidebar.download_button(
        "Download",
        convert_image(processed_image),
        "background_removed.png",
        "image/png"
    )

uploaded_image = st.sidebar.file_uploader("Upload", type=["png", "jpg", "jpeg"])

if uploaded_image:
    if st.sidebar.button("Process"):
        process_image(upload=uploaded_image)
