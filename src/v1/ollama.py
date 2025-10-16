import inspect
from ollama import chat, list as list_models
from services.logger import Logger

class Ollama:

    DEFAULT_MODEL = "llama3:latest"

    def GenerateFeedback(resume_text, jd_text):

        prompt = (
            f"You are an expert career coach. Analyze the following resume and job description.\n\n"
            f"--- Resume ---\n{resume_text}\n\n"
            f"--- Job Description ---\n{jd_text}\n\n"
            f"Provide feedback on how well the resume fits the job and give 3 specific improvement suggestions."
        )

        try:
            res = chat(model=Ollama.DEFAULT_MODEL, messages=[{"role": "user", "content": prompt}])
            message = res.get("message", {})
            
            return message.get("content", "No feedback generated")
        
        except Exception as e:
            print(str(e))
            Logger.CreateExceptionLog(inspect.stack()[0][3],str(e),'Failed to generate feedback')

            return res.get("message", {}).get("content", "No feedback generated")