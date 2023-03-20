"""
H_language = LanguageEncoder(X_language)
H_vision = W_h * VisionExtractor(X_vision)
"""
import torch
from transformers import T5Tokenizer, T5Model
class LanguageEncoder(torch.nn):
    """
    Encodes input strings to transformer embeddings.
    """

    def __init__(self, lang_model_id="GPT2") -> None:
        self.transformer = T5Model



class MultiModal(torch.nn)