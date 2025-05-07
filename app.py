from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fragen und Antworten
questions = [
    {"question": "Was ist die Hauptstadt von Deutschland?", "answer": "Berlin"},
    {"question": "Wie viele Beine hat eine Spinne?", "answer": "8"},
    {"question": "Was ist 5 + 7?", "answer": "12"},
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            user_answer = request.form.get(f"q{i}")
            if user_answer and user_answer.strip().lower() == q["answer"].lower():
                score += 1
        return render_template("result.html", score=score, total=len(questions))
    
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
