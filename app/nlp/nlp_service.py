import spacy
from typing import Dict, Any

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def process_text(text: str) -> Dict[str, Any]:
    """
    Process text using spaCy to extract tokens and their POS tags
    
    Args:
        text: The input text to process
        
    Returns:
        A dictionary containing the processed results
    """
    doc = nlp(text)
    
    tokens = []
    for token in doc:
        tokens.append({
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "is_stop": token.is_stop,
            "is_alpha": token.is_alpha,
            "is_punct": token.is_punct
        })
    
    sentences = []
    for sent in doc.sents:
        sentences.append(sent.text)
    
    return {
        "tokens": tokens,
        "sentences": sentences,
        "text": text
    }
