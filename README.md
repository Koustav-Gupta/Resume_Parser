# Resume_Parser

📄 Automated Resume Parser
An NLP-based tool that extracts useful information like Name, Email, and Skills from uploaded resumes in PDF format.

🚀 Features
Upload PDF resumes via web UI
Extract name, email, and skills using spaCy
Modular code with easily expandable skill detection

🛠️ Tech Stack
Python
Flask
spaCy
PDFPlumber

📁 Project Structure
resume_parser/
├── app.py
├── parser/
│   └── extractor.py
├── templates/
│   └── index.html
├── uploads/
├── requirements.txt
└── README.md

⚙️ Installation
git clone https://github.com/YOUR_USERNAME/resume-parser.git
cd resume-parser
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
Then open http://127.0.0.1:5000 in your browser.

📦 Deployment on Render
Create a new Web Service at Render
Use your GitHub repo
Set the build and start command:
Build Command: pip install -r requirements.txt && python -m spacy download en_core_web_sm
Start Command: python app.py
Optional: Add uploads/ to .gitignore if not needed in repo

📝 License
MIT License
