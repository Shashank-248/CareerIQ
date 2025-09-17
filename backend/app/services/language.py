from langdetect import detect
from typing import Dict

SUPPORTED = {"en": "English", "hi": "Hindi", "te": "Telugu"}

# Very lightweight placeholder translation (identity / echo) - extend later
class TranslationService:
    def translate(self, text: str, target_lang: str) -> Dict:
        # In prototype: just return original unless different language
        return {"original": text, "translated": text, "detected": self.detect_language(text), "target": target_lang, "confidence": 0.75}

    def detect_language(self, text: str) -> str:
        try:
            code = detect(text)
            if code.startswith("hi"):
                return "hi"
            if code.startswith("te"):
                return "te"
            return "en"
        except Exception:
            return "en"
