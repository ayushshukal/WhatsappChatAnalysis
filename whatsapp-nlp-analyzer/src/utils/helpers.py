"""General helper functions shared across the project."""

import importlib.util

# pip package name -> import name (they differ for scikit-learn)
REQUIRED_PACKAGES = {
    "streamlit": "streamlit",
    "pandas": "pandas",
    "numpy": "numpy",
    "nltk": "nltk",
    "spacy": "spacy",
    "scikit-learn": "sklearn",
    "plotly": "plotly",
    "matplotlib": "matplotlib",
    "wordcloud": "wordcloud",
    "emoji": "emoji",
}

SPACY_MODEL = "en_core_web_sm"

# NLTK resource name -> path NLTK uses to locate it
NLTK_RESOURCES = {
    "punkt": "tokenizers/punkt",
    "punkt_tab": "tokenizers/punkt_tab",
    "stopwords": "corpora/stopwords",
    "vader_lexicon": "sentiment/vader_lexicon.zip",
}


def check_packages() -> dict:
    """Return {package: True/False} depending on whether it is installed.

    Uses find_spec so the heavy libraries are not actually imported.
    """
    return {
        pip_name: importlib.util.find_spec(import_name) is not None
        for pip_name, import_name in REQUIRED_PACKAGES.items()
    }


def check_spacy_model(model_name: str = SPACY_MODEL) -> bool:
    """Return True if spaCy and the given language model are installed."""
    if importlib.util.find_spec("spacy") is None:
        return False
    try:
        import spacy

        return spacy.util.is_package(model_name)
    except Exception:
        return False


def check_nltk_resources() -> dict:
    """Return {resource: True/False} for the NLTK data we will need."""
    if importlib.util.find_spec("nltk") is None:
        return {name: False for name in NLTK_RESOURCES}

    import nltk

    status = {}
    for name, path in NLTK_RESOURCES.items():
        try:
            nltk.data.find(path)
            status[name] = True
        except LookupError:
            status[name] = False
    return status
