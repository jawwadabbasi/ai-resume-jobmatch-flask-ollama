import io
from pypdf import PdfReader
from docx import Document

class Parser:
    
    def FromPdf(file_bytes: bytes) -> str:
        
        reader = PdfReader(io.BytesIO(file_bytes))
        text = []
        
        for page in reader.pages:
            text.append(page.extract_text() or "")
        
        return "\n".join(text).strip()

    def FromDocx(file_bytes: bytes) -> str:
        
        doc = Document(io.BytesIO(file_bytes))
        
        return "\n".join(p.text for p in doc.paragraphs).strip()

    def FromText(text: str) -> str:
        
        return (text or "").strip()