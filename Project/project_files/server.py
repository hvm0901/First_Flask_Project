from flask import Flask, render_template

from project_files.translator import englishToFrench, frenchToEnglish

app = Flask("Translator")

def index():
    return render_template("index.html")

@app.route("/french/<english_text>")
def french_endpoint(english_text):
    return englishToFrench(englishText=english_text)


@app.route("/english/<french_text>")
def english_endpoint(french_text):
    return frenchToEnglish(frenchText=french_text)


if __name__ == "__main__":
    app.run(debug=True)
