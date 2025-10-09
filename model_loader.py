import streamlit as st
from transformers import pipeline

MODEL_NAME = "j-hartmann/emotion-english-distilroberta-base"

EMOTION_MAPPING = {
    "joy": {"emoji": "😀", "color": "green", "vibe": "Upbeat, High-Tempo Pop"},
    "sadness": {"emoji": "😭", "color": "blue", "vibe": "Acoustic, Soft Piano Ballads"},
    "anger": {"emoji": "😡", "color": "red", "vibe": "High-Energy Rock, Aggressive EDM"},
    "fear": {"emoji": "😨", "color": "orange", "vibe": "Calm Ambient, Classical Focus"},
    "disgust": {"emoji": "🤢", "color": "purple", "vibe": "Calm Ambient, Classical Focus"},
    "surprise": {"emoji": "😮", "color": "yellow", "vibe": "Experimental, Exciting Electronic Beats"},
    "neutral": {"emoji": "😐", "color": "gray", "vibe": "Lo-Fi Beats, Deep Focus Music"},
}

@st.cache_resource
def get_classifier(MODEL_NAME, EMOTION_MAPPING):
    classifier = pipeline("text-classification", model=MODEL_NAME, tokenizer=MODEL_NAME)
    return classifier, EMOTION_MAPPING

def predict_emotion(text, MODEL_NAME, EMOTION_MAPPING):
    classifier, mapping = get_classifier(MODEL_NAME, EMOTION_MAPPING)
    result = classifier(text)[0]
    label = result["label"].lower()
    emotion_data = mapping.get(label, {"emoji": "❓", "color": "gray", "vibe": "Unknown"})
    
    return {
        "label": label,
        "score": result["score"],
        "emoji": emotion_data["emoji"],
        "color": emotion_data["color"],
        "vibe": emotion_data["vibe"]
    }