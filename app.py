from flask import Flask, render_template_string, request
import explorerhat
import time
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🏆 COMP1313 Interactive Quiz</title>
    <style>
        body { font-family: Arial; text-align: center; background-color: #f4f4f4; margin-top: 50px; }
        button { padding: 10px 20px; margin: 5px; background-color: #2196f3; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #1976d2; }
        .message { font-size: 22px; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>🏆 Interactive Quiz System</h1>
    
    {% if not answered %}
        <div class="question-box">
            <h2>{{ q['question'] }}</h2>
            <form method="POST">
                {% for opt in q['options'] %}
                    <button type="submit" name="answer" value="{{ opt }}">{{ opt }}</button>
                {% endfor %}
                <input type="hidden" name="correct" value="{{ q['answer'] }}">
            </form>
        </div>
    {% else %}
        <div class="message">{{ message }}</div>
        <meta http-equiv="refresh" content="2"> {% endif %}
</body>
</html>
"""

# Sample Questions
questions = [
    {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Personal Unit"], "answer": "Central Processing Unit"},
    {"question": "Which is volatile memory?", "options": ["RAM", "ROM", "SSD"], "answer": "RAM"}
] [cite: 284, 287, 299]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected = request.form["answer"]
        correct = request.form["correct"]

        if selected == correct:
            # CORRECT: Blue LED (OUT2) ON for 2 seconds
            explorerhat.output.two.on() [cite: 313]
            time.sleep(2)
            explorerhat.output.two.off() [cite: 315]
            return render_template_string(HTML, answered=True, message="✅ Correct! Blue LED is ON.", q=None)
        else:
            # INCORRECT: Red LED (OUT3) + Buzzer (OUT1) ON for 1 second
            explorerhat.output.three.on() [cite: 319]
            explorerhat.output.one.on() [cite: 320]
            time.sleep(1)
            explorerhat.output.three.off() [cite: 322]
            explorerhat.output.one.off() [cite: 323]
            return render_template_string(HTML, answered=True, message="❌ Incorrect! Red LED + Buzzer.", q=None)

    # GET Request: Load a random question
    q = random.choice(questions) [cite: 327]
    return render_template_string(HTML, q=q, answered=False, message=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
