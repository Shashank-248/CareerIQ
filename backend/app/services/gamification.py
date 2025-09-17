from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Badge:
    code: str
    name: str
    criteria: str

BADGE_CATALOG = [
    Badge(code="first_skill", name="First Skill Logged", criteria=">=1 skill added"),
    Badge(code="five_skills", name="Skill Collector", criteria=">=5 skills"),
    Badge(code="challenge_start", name="Challenger", criteria="First challenge attempted")
]

class GamificationEngine:
    def evaluate(self, profile) -> Dict:
        badges = []
        skill_count = len(profile.skills)
        if skill_count >= 1:
            badges.append("first_skill")
        if skill_count >= 5:
            badges.append("five_skills")
        # Placeholder points based on average skill score
        avg = int(sum(s.score for s in profile.skills)/len(profile.skills)) if profile.skills else 0
        return {"points": avg * 10, "badges": badges}
