# app.py

import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# 1️⃣ Load the pretrained model (English → Hindi)
@st.cache_resource  # caches the model to avoid reloading each run
def load_model():
    model_name = "Helsinki-NLP/opus-mt-en-hi"  # public model
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()

# 2️⃣ Translation function with beam search
def translate(text):
    inputs = tokenizer([text], return_tensors="pt", padding=True)
    translated = model.generate(
        **inputs,
        max_length=128,
        num_beams=5,       # improves translation quality
        early_stopping=True
    )
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# 3️⃣ Streamlit UI
st.title("🌍 English → Hindi Translator")

# Input area for English text
english_text = st.text_area("Enter English text here:")

# Translate button
if st.button("Translate"):
    if english_text.strip() != "":
        hindi_translation = translate(english_text)
        st.markdown(f"**English:** {english_text}")
        st.markdown(f"**Translated (Hindi):** {hindi_translation}")
    else:
        st.warning("⚠️ Please enter some English text!")
