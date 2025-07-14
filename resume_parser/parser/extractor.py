import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return " ".join([page.extract_text() or "" for page in pdf.pages])

def extract_entities(text):
    doc = nlp(text)
    data = {"name": "", "email": "", "skills": []}
    for ent in doc.nets:
        if ent.label_ == "PERSON" and not data["name"]:
            data["name"] = ent.text
        elif "@" in ent.text:
            data["email"] = ent.text
    skills = ["Python", "Java", "C++", "SQL", "Machine Learning"]
    data["skills"] = [skill for skill in skills if skill.lower() in text.lower()]
    return data