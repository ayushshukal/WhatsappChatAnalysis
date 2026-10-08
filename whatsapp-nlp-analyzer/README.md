# WhatsApp Group Chat Analyzer (NLP)

A Streamlit web app that analyses an exported WhatsApp group chat using
traditional NLP and machine learning. No LLMs, chatbots, RAG or external AI APIs.

> **Status:** Phase 1 of 12 (project skeleton). Features are added phase by phase.

## Planned features
- WhatsApp chat parsing (multiline messages, system messages, media placeholders)
- Text preprocessing, tokenization and stopword removal
- Chat statistics, participant analysis and timeline analysis
- Sentiment analysis and emotion analysis
- Topic modeling with LDA
- Word frequency, TF-IDF and emoji analysis
- Named Entity Recognition with spaCy
- Interactive Plotly dashboard
- Evaluation: parser accuracy, sentiment/emotion metrics, topic quality

## Privacy
- Chats are processed **locally**. Nothing is sent to external APIs.
- Real chat files are git-ignored (`data/raw/`, `data/processed/`). Never commit them.
- Use anonymized names in screenshots, demos and documentation.
- Streamlit may collect anonymous usage statistics (never chat content). To disable,
  create `.streamlit/config.toml` containing:
```toml
  [browser]
  gatherUsageStats = false
```

## Tech stack
Python 3.10+ (3.11 or 3.12 recommended), Streamlit, pandas, numpy, NLTK, spaCy,
scikit-learn, Plotly, Matplotlib, WordCloud, emoji.

## Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

python -m spacy download en_core_web_sm
python -m nltk.downloader punkt punkt_tab stopwords vader_lexicon
```

## Run
```bash
streamlit run app.py
```
Then open http://localhost:8501.

## Project structure
```text
app.py            Streamlit entry point
src/parser/       WhatsApp chat parser
src/preprocessing/ Cleaning and tokenization
src/analysis/     Statistics, sentiment, emotion, topics, words, emojis, NER
src/utils/        Shared helpers
ui/               Dashboard layout, charts, styles
tests/            Unit tests
notebooks/        Exploration notebooks
data/             Local-only chat data (git-ignored)
models/           Local-only saved models (git-ignored)
```

## Team
_Add team member names and course details here._
