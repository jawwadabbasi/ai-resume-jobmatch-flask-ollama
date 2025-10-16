# AI Resume JobMatch (Flask + Ollama + MySQL)

An intelligent resume analysis API built with **Flask**, **Ollama**, and **MySQL**.  
It compares a candidate’s resume against a given job description, calculates a compatibility score using semantic AI models, and provides **personalized improvement feedback** powered by local LLMs (like Llama 3).

---

## Features

- Upload a resume (PDF) and paste a job description (text)
- AI-based semantic similarity scoring using `sentence-transformers`
- Multi-factor evaluation: content overlap, resume completeness, and contextual fit
- Llama 3 integration (via Ollama) for personalized feedback
- Results stored in MySQL (with JSON-based meta fields)
- Docker-ready for deployment

---

## Tech Stack

- **Backend:** Flask (Python 3.13)
- **AI / NLP:** `sentence-transformers`, `Ollama (Llama 3)`
- **Database:** MySQL
- **Containerization:** Docker
- **Logging:** Custom logger + Sentry support

---

## Project Structure

```
.
├── LICENSE
├── README.md
├── dev/
│   ├── Dockerfile
│   ├── kubeconfig.yaml
│   └── settings.py
├── prod/
│   ├── Dockerfile
│   ├── kubeconfig.yaml
│   └── settings.py
└── src/
    ├── main.py                 # Flask entrypoint
    ├── includes/               # Common helpers and DB logic
    ├── services/               # Logging and cron jobs
    ├── v1/                     # Core logic (Resume, Analysis, Ollama, Parser, etc.)
    └── v2/                     # Placeholder for future upgrades
```

---

## API Usage

### Endpoint
`POST /api/v1/Analyze/Resume`

### Form Data
| Key | Type | Description |
|-----|------|--------------|
| `Resume` | File (PDF) | The candidate's resume |
| `JobDescription` | Text | The target job description |

### Example Response
```json
{
  "ApiHttpResponse": 201,
  "ApiMessages": ["Request processed successfully"],
  "ApiResult": [
    {
      "ScoreOverall": 84.5,
      "Summary": "Good match — some fine-tuning could make this even stronger.",
      "ScoreSemanticSimilarity": 79.8,
      "ScoreLengthBalance": 95.2,
      "Feedback": "Your resume aligns well but could include more details on backend frameworks and leadership experience."
    }
  ]
}
```

---

## Setup Instructions

### Clone the repository
```bash
git clone https://github.com/jawwadabbasi/ai-resume-jobmatch-flask-ollama.git
cd ai-resume-jobmatch-flask-ollama
```

### Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```bash
pip install -r src/requirements.txt
```

### Start Ollama and pull the model
```bash
ollama pull llama3
```

### Run the Flask app
```bash
python3 src/main.py
```

The API will be available at:  
**http://127.0.0.1:8000/api/v1/Analyze/Resume**

---

## License

This project is licensed under the **MIT License** — free for personal and commercial use.

---

## Author

**Built with ingenuity,**  
by **Jawwad Abbasi** ([@jawwadabbasi](https://github.com/jawwadabbasi))  
Email: `jawwad@kodelle.com`