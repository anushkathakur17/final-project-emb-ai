"""
Emotion Detection Flask Server
"""

from flask import Flask
from flask import render_template
from flask import request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def analyze_emotion():
    """
    Analyze emotion from user text.
    """

    text_to_analyze = request.args.get(
        "textToAnalyze"
    )

    response = emotion_detector(
        text_to_analyze
    )

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    result = (
        f"For the given statement, "
        f"the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

    return result


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
    