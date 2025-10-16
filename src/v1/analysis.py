import re
import math
from typing import Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Analysis:

    SKILL_HINTS = [
        "python", "flask", "django", "fastapi", "mysql", "postgresql", "aws",
        "docker", "kubernetes", "react", "node", "redis", "stripe", "twilio",
        "devops", "ci/cd", "terraform", "gcp", "azure", "selenium", "api"
    ]

    EXP_HINTS = ["years", "experience", "built", "developed", "designed", "led"]

    EDU_HINTS = ["bachelor", "master", "bs", "ms", "degree", "computer science", "b.sc", "bsc", "msc"]

    def TfidfCosine(a: str, b: str) -> float:
        
        v = TfidfVectorizer(stop_words="english")
        X = v.fit_transform([a, b])
        sim = cosine_similarity(X[0:1], X[1:2])[0][0]
        
        return round(float(sim * 100), 2)

    def BucketScore(text: str, hints) -> float:
        
        text_l = text.lower()
        hits = sum(1 for h in hints if h in text_l)
        denom = max(len(hints), 1)
        
        return round((hits / denom) * 100, 2)

    def Run(resume_text: str, jd_text: str) -> Dict:
        
        overall = Analysis.TfidfCosine(resume_text, jd_text)

        skills_resume = Analysis.BucketScore(resume_text, Analysis.SKILL_HINTS)
        skills_jd = Analysis.BucketScore(jd_text, Analysis.SKILL_HINTS)
        skills = round((0.6 * skills_resume + 0.4 * skills_jd), 2)

        exp = Analysis.BucketScore(resume_text, Analysis.EXP_HINTS)
        edu = Analysis.BucketScore(resume_text, Analysis.EDU_HINTS)

        overall_blend = round(0.5 * overall + 0.3 * skills + 0.2 * max(exp, edu), 2)

        summary = (
            f"Overall fit: {overall_blend}%. "
            f"Skills alignment: {skills}%. "
            f"Experience signal: {exp}%. "
            f"Education signal: {edu}%."
        )

        return {
            "ScoreOverall": overall_blend,
            "ScoreSkills": skills,
            "ScoreExperience": exp,
            "ScoreEducation": edu,
            "Summary": summary
        }