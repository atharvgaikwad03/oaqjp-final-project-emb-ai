"""
Flask server for the Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_function():
    """Analyse the emotion of the text passed as a query parameter."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': "
            f"{response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']}, "
            f"'sadness': {response['sadness']}. The dominant emotion is "
            f"{response['dominant_emotion']}."
        )

    return response_text


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
