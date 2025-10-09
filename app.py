import streamlit as st
from model_loader import predict_emotion, EMOTION_MAPPING, MODEL_NAME

PLAYLIST_EMBEDS = {
    "joy": "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC?utm_source=generator",
    "sadness": "https://open.spotify.com/embed/playlist/25ZzkJkOuYir9kHr2CqwPQ?utm_source=generator",
    "anger": "https://open.spotify.com/embed/playlist/67STztGl7srSMNn6hVYPFR?utm_source=generator",
    "fear": "https://open.spotify.com/embed/playlist/37i9dQZF1DX1g0iEXLFycr?utm_source=generator",
    "disgust": "https://open.spotify.com/embed/playlist/37i9dQZF1DX9uKNf5jGX6m?utm_source=generator",
    "surprise": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0SM0LYsmbMT?utm_source=generator",
    "neutral": "https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M?utm_source=generator"
}

st.set_page_config(
    page_title="Mood-Based Playlist Curator",
    page_icon="🎶",
    layout="centered"
)

st.title("🎶 Real-time Mood-Based Playlist Curator")
st.markdown("### Tell me how you feel, and I'll recommend music based on your emotion.")

user_text = st.text_area(
    "Describe your current mood or a recent thought:",
    placeholder="Example: I just finished a huge presentation and feel relieved and happy!",
    height=100
)

if st.button("Analyze Mood & Curate Playlist", type="primary"):
    if user_text:
        with st.spinner("Analyzing your mood..."):
            result = predict_emotion(user_text, MODEL_NAME, EMOTION_MAPPING)
            predicted_emotion = result["label"]
            confidence = result["score"]

        emotion_key = predicted_emotion.lower()
        
        emotion_data = EMOTION_MAPPING.get(emotion_key, EMOTION_MAPPING['neutral'])
        embed_url = PLAYLIST_EMBEDS.get(emotion_key, PLAYLIST_EMBEDS['neutral'])
        
        emoji = emotion_data['emoji']
        vibe = emotion_data['vibe']

        st.divider()
        st.header(f"Result: {emoji} {emotion_key.capitalize()} {emoji}")

        st.markdown(
            f"Your primary mood is identified as **{emotion_key.capitalize()}** with **{confidence*100:.1f}% confidence**."
        )

        st.info(f"The curator suggests a **{vibe}** playlist to match this feeling.")
        
        st.subheader("🎵 Curated Vibe")
        st.components.v1.html(
            f"""
            <iframe src="{embed_url}" 
                width="100%" 
                height="352" 
                frameborder="0" 
                allowtransparency="true" 
                allow="encrypted-media">
            </iframe>
            """,
            height=370
        )
    else:
        st.error("Please enter some text to analyze your mood!")

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Project:** Real-time Mood Curator")
st.sidebar.markdown(f"**ML Model:** DistilRoBERTa (Emotion Classification)")
st.sidebar.markdown(f"**Innovation:** Mapping predicted emotion to curated content using minimal code.")