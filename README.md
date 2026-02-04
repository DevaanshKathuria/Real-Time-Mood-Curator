# Real-time Mood-Based Playlist Curator

This is a small but impactful Machine Learning project that translates a user's natural language text input (describing their mood) into a classified emotion, which is then mapped to a curated music playlist/vibe.

The application is built entirely in Python and deployed using Streamlit for a simple, interactive web interface.

## Features

- **Real-time Emotion Classification**: Uses a pre-trained DistilRoBERTa model (via the Hugging Face transformers library) to classify user text into one of seven detailed emotions: joy, sadness, anger, fear, disgust, surprise, or neutral.

- **Minimalist ML**: Achieves strong performance without needing local model training, relying on fast inference from a small, cached model.

- **Curated Vibe Mapping**: Dynamically maps the predicted emotion to a suggested music genre and provides an embeddable link, making the output immediately actionable and engaging.

- **Simple Deployment**: Built with Streamlit, requiring no front-end code (HTML/CSS/JavaScript).

## How to Run Locally

Follow these steps to set up and run the app on your local machine.

### 1. Prerequisites

Install Streamlit and other dependencies
```bash
pip install -r requirements.txt
You must have Python 3.8+ installed on your system.
```

### 2. Setup the Project

First, clone the repository (or ensure you have the three files: app.py, model_loader.py, and requirements.txt in a single folder).

Clone the repository
```bash
git clone <repository-url>
cd <repository-name>
```

Create and navigate to the project directory
```bash
mkdir Mood_Curator
cd Mood_Curator
```

### 3. Install Dependencies

Install all required Python packages (including streamlit, transformers, and torch). It is highly recommended to use a virtual environment (venv).

1. (Optional but recommended) Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Use 'venv\Scripts\activate' on Windows Command Prompt
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Streamlit application using the Streamlit CLI command.

```bash
streamlit run app.py
```

This command will automatically open the web application in your default browser (usually at http://localhost:8501).

## Project Structure

The project maintains a minimal, clean structure as per the design constraints:

```
Mood_Curator/
├── app.py              # The main Streamlit file (UI and logic orchestration).
├── model_loader.py     # Caches and handles all ML model inference logic.
└── requirements.txt    # Lists all Python dependencies.
```

## ML Model Details

The app uses the j-hartmann/emotion-english-distilroberta-base model from Hugging Face. This model is a DistilRoBERTa checkpoint fine-tuned on diverse English text datasets for multi-class emotion classification. This approach ensures high accuracy while keeping the application lightweight and fast for deployment.
