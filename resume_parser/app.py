from flask import Flask, request, render_template
from parser.extractor import extract_text_from_pdf, extract_entities
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    data = {}
    if request.method == "POST":
        file = request.files["resume"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        text = extract_text_from_pdf(filepath)
        data = extract_entities(text)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)