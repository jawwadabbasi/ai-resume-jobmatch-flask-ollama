import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from v1.ollama import Ollama

class Analysis:

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    @staticmethod
    def Run(resume_text, jd_text):

        embeddings = Analysis.model.encode([resume_text, jd_text])
        sim = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        similarity_score = round(sim * 100, 2)

        length_penalty = min(len(resume_text) / len(jd_text), 1.0) * 100
        relevance_score = round((similarity_score * 0.8 + length_penalty * 0.2), 2)

        if relevance_score > 85:
            verdict = "Excellent match — your resume strongly aligns with this role."
        
        elif relevance_score > 65:
            verdict = "Good match — some fine-tuning could make this even stronger."
        
        elif relevance_score > 45:
            verdict = "Partial match — the role may require skills not fully reflected."
        
        else:
            verdict = "Weak match — significant differences between resume and job."

        return {
            "ScoreOverall": relevance_score,
            "Summary": verdict,
            "ScoreSemanticSimilarity": similarity_score,
            "ScoreLengthBalance": round(length_penalty, 2),
            "Feedback": Ollama.GenerateFeedback(resume_text, jd_text) 
        }