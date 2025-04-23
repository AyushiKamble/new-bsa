import streamlit as st
import numpy as np
from PIL import Image
import io

st.title("Blood Spatter Pattern Analyzer")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
scale_factor = st.number_input("Scale Factor (units per pixel):", value=1.0, step=0.01)

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    st.image(image_np, caption="Uploaded Image", use_column_width=True)

    st.subheader("Select Two Points for Distance Measurement")
    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Point 1 - X:", min_value=0, value=0)
        y1 = st.number_input("Point 1 - Y:", min_value=0, value=0)

    with col2:
        x2 = st.number_input("Point 2 - X:", min_value=0, value=0)
        y2 = st.number_input("Point 2 - Y:", min_value=0, value=0)

    if st.button("Calculate Distance"):
        distance_pixels = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance_real = distance_pixels * scale_factor
        st.success(f"Distance: {distance_real:.2f} units")
