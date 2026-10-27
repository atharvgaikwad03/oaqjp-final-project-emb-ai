"""
Flask server for the Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyse the emotion of the text passed as a query parameter.
    Returns a formatted string with emotion scores and dominant emotion.
    """
    text_to_analyse = request.args.get('textToAnalyse')

    if not text_to_analyse or text_to_analyse.strip() == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant}</b>."
    )


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
