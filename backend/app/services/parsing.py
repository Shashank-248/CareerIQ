from typing import List, Dict
import re

TECH_KEYWORDS = [
    "python", "sql", "excel", "machine learning", "ml", "data analysis", "c++", "java", "javascript", "react", "cloud", "gcp", "aws", "azure",
    # Added AI-related terms
    "ai", "artificial intelligence", "generative ai", "llm", "nlp", "deep learning"
]

class ResumeParser:
    def extract_text(self, content: bytes, filename: str) -> str:
        # Placeholder: naive decode
        try:
            return content.decode("utf-8", errors="ignore")
        except Exception:
            return ""

    def infer_skills(self, text: str) -> List[Dict]:
        found = []
        lower = re.sub(r"[,.()]", " ", text.lower())
        seen = set()
        for kw in TECH_KEYWORDS:
            pattern = r"\b" + re.escape(kw) + r"\b"
            if re.search(pattern, lower):
                key_norm = kw.lower()
                if key_norm in seen:
                    continue
                seen.add(key_norm)
                found.append({
                    "name": kw.title(),
                    "score": 60,
                    "evidence": ["resume"],
                    "last_updated": None
                })
        return found
