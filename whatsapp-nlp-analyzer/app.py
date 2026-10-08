"""
WhatsApp NLP Analyzer - Streamlit entry point.

Phase 1: layout only. The sidebar, tabs and environment check work,
but no chat is parsed or analysed yet.
"""

import streamlit as st

from src.utils.helpers import (
    SPACY_MODEL,
    check_nltk_resources,
    check_packages,
    check_spacy_model,
)

APP_TITLE = "WhatsApp NLP Analyzer"

# Analyses the user can switch on/off in the sidebar.
ANALYSIS_OPTIONS = [
    "Statistics",
    "Sentiment",
    "Emotion",
    "Topics",
    "Word Analysis",
    "Emoji Analysis",
    "NER",
]

# Tab name -> what will appear there (and in which phase).
TABS = {
    "Overview": "Summary cards and activity charts (Phases 4 and 10).",
    "Participants": "Per-user message and word statistics (Phases 4 and 10).",
    "Text Analysis": "Frequent words and word clouds (Phase 8).",
    "Sentiment": "Positive / neutral / negative distribution (Phase 5).",
    "Emotion": "Emotion distribution by participant and time (Phase 6).",
    "Topics": "LDA topic modelling (Phase 7).",
    "Emojis": "Emoji frequency and per-user usage (Phase 8).",
    "Named Entities": "People, places, organisations and dates (Phase 9).",
    "Timeline": "Activity by date, weekday, hour and month (Phases 4 and 10).",
}


@st.cache_data
def run_environment_check() -> dict:
    """Check packages and NLP resources. Cached so it runs only once."""
    return {
        "packages": check_packages(),
        "spacy_model": check_spacy_model(),
        "nltk": check_nltk_resources(),
    }


def render_sidebar():
    """Draw the sidebar. Returns (uploaded_file, {option_name: is_checked})."""
    st.sidebar.title(APP_TITLE)

    st.sidebar.header("Upload Chat")
    uploaded_file = st.sidebar.file_uploader(
        "Upload .txt",
        type=["txt"],
        help="Export a chat from WhatsApp and upload the .txt file. "
        "It is processed locally and never sent to any external service.",
    )

    st.sidebar.header("Analysis Options")
    selected = {
        name: st.sidebar.checkbox(name, value=True) for name in ANALYSIS_OPTIONS
    }
    return uploaded_file, selected


def render_environment_check():
    """Show an expander telling the user what is installed and what is missing."""
    status = run_environment_check()
    missing_packages = [n for n, ok in status["packages"].items() if not ok]
    missing_nltk = [n for n, ok in status["nltk"].items() if not ok]
    all_ok = not missing_packages and status["spacy_model"] and not missing_nltk

    # Open automatically only when something needs fixing.
    with st.expander("Environment check", expanded=not all_ok):
        if missing_packages:
            st.error(
                "Missing Python packages: " + ", ".join(missing_packages)
                + ". Run: `pip install -r requirements.txt`"
            )
        else:
            st.success("All required Python packages are installed.")

        if status["spacy_model"]:
            st.success(f"spaCy model `{SPACY_MODEL}` is installed.")
        else:
            st.warning(
                f"spaCy model `{SPACY_MODEL}` not found. "
                f"Run: `python -m spacy download {SPACY_MODEL}`"
            )

        if missing_nltk:
            st.warning(
                "Missing NLTK resources: " + ", ".join(missing_nltk)
                + ". Run: `python -m nltk.downloader punkt punkt_tab stopwords vader_lexicon`"
            )
        else:
            st.success("All required NLTK resources are downloaded.")

        if st.button("Re-check"):
            run_environment_check.clear()
            st.rerun()


def main():
    """Build the page."""
    st.set_page_config(page_title=APP_TITLE, page_icon="💬", layout="wide")

    uploaded_file, selected_options = render_sidebar()

    st.title(f"💬 {APP_TITLE}")
    st.caption(
        "Group chat analysis using traditional NLP: preprocessing, sentiment, "
        "emotion, LDA topics, NER and more. Everything runs locally."
    )

    render_environment_check()

    if uploaded_file is None:
        st.info("Upload an exported WhatsApp chat (.txt) in the sidebar to begin.")
    else:
        size_kb = uploaded_file.size / 1024
        st.success(
            f"Received **{uploaded_file.name}** ({size_kb:.1f} KB). "
            "Parsing will be added in Phase 2."
        )
        enabled = [name for name, checked in selected_options.items() if checked]
        st.write("Enabled analyses:", ", ".join(enabled) if enabled else "none")

    # One tab per dashboard section; each is a placeholder for now.
    tab_objects = st.tabs(list(TABS))
    for tab, (name, description) in zip(tab_objects, TABS.items()):
        with tab:
            st.subheader(name)
            st.info(f"Coming soon: {description}")


if __name__ == "__main__":
    main()
