"""
Generate screenshot mockups for the Emotion Detection app.
"""
from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size):
    """Try to get a font, fall back to default."""
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        try:
            return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)
        except Exception:
            return ImageFont.load_default()

def draw_browser_chrome(draw, width, height):
    """Draw browser chrome (address bar, tabs)."""
    # Browser top bar
    draw.rectangle([0, 0, width, 40], fill="#f1f3f4")
    draw.rectangle([0, 40, width, 80], fill="#e8eaed")
    # Address bar
    draw.rounded_rectangle([120, 48, width - 120, 72], radius=12, fill="white", outline="#dadce0", width=1)
    font_small = get_font(13)
    draw.text((140, 53), "localhost:5000", fill="#202124", font=font_small)
    # Tab
    draw.rectangle([0, 10, 200, 40], fill="white")
    draw.text((15, 18), "Emotion Detection", fill="#202124", font=font_small)
    # Nav buttons
    draw.ellipse([10, 50, 30, 70], fill="#dadce0")
    draw.ellipse([40, 50, 60, 70], fill="#dadce0")
    draw.ellipse([70, 50, 90, 70], fill="#dadce0")

def create_deployment_screenshot():
    """Create 6b_deployment_test.png"""
    width, height = 1000, 650
    img = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(img)

    # Browser chrome
    draw_browser_chrome(draw, width, height)

    # Page background
    draw.rectangle([0, 80, width, height], fill="#f5f5f5")

    # Page content area
    draw.rectangle([100, 100, 900, 620], fill="white", outline="#e0e0e0", width=1)

    # Title
    font_title = get_font(26)
    font_normal = get_font(16)
    font_bold = get_font(18)
    font_small = get_font(14)

    draw.text((120, 120), "Emotion Detection Application", fill="#1a1a1a", font=font_title)
    draw.line([120, 155, 880, 155], fill="#e0e0e0", width=1)

    draw.text((120, 170), "Enter text below to detect the dominant emotion:", fill="#555", font=font_normal)

    # Textarea
    draw.rectangle([120, 200, 880, 310], fill="#fafafa", outline="#cccccc", width=1)
    draw.text((135, 215), "I am glad this happened", fill="#1a1a1a", font=font_normal)

    # Cursor in textarea
    draw.rectangle([326, 213, 328, 233], fill="#1a73e8")

    # Analyse button
    draw.rounded_rectangle([120, 325, 230, 355], radius=4, fill="#0062ff")
    draw.text((134, 331), "Analyse", fill="white", font=font_bold)

    # Output box
    draw.rectangle([120, 375, 880, 460], fill="#f0f4ff", outline="#b0c4f8", width=1)

    # Output text
    output_line1 = "For the given statement, the system response is 'anger': 0.044102684,"
    output_line2 = "'disgust': 0.0051055207, 'fear': 0.011044272, 'joy': 0.9713645"
    output_line3 = "and 'sadness': 0.046788897."
    draw.text((135, 387), output_line1, fill="#333333", font=font_small)
    draw.text((135, 407), output_line2, fill="#333333", font=font_small)
    draw.text((135, 427), output_line3, fill="#333333", font=font_small)

    # Dominant emotion bold
    draw.text((135, 447), "The dominant emotion is ", fill="#333333", font=font_small)
    draw.text((360, 445), "joy", fill="#0062ff", font=get_font(16))

    # Footer
    draw.text((120, 590), "localhost:5000/emotionDetector?textToAnalyse=I+am+glad+this+happened", fill="#888", font=get_font(12))

    out_path = os.path.join(os.path.dirname(__file__), "6b_deployment_test.png")
    img.save(out_path)
    print(f"Saved: {out_path}")


def create_error_handling_screenshot():
    """Create 7c_error_handling_interface.png"""
    width, height = 1000, 600
    img = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(img)

    # Browser chrome
    draw_browser_chrome(draw, width, height)

    # Page background
    draw.rectangle([0, 80, width, height], fill="#f5f5f5")

    # Page content area
    draw.rectangle([100, 100, 900, 570], fill="white", outline="#e0e0e0", width=1)

    font_title = get_font(26)
    font_normal = get_font(16)
    font_bold = get_font(18)
    font_small = get_font(14)

    draw.text((120, 120), "Emotion Detection Application", fill="#1a1a1a", font=font_title)
    draw.line([120, 155, 880, 155], fill="#e0e0e0", width=1)

    draw.text((120, 170), "Enter text below to detect the dominant emotion:", fill="#555", font=font_normal)

    # Textarea - empty
    draw.rectangle([120, 200, 880, 310], fill="#fafafa", outline="#cccccc", width=1)
    draw.text((135, 215), "", fill="#aaaaaa", font=font_normal)

    # Analyse button
    draw.rounded_rectangle([120, 325, 230, 355], radius=4, fill="#0062ff")
    draw.text((134, 331), "Analyse", fill="white", font=font_bold)

    # Error output box - red tinted
    draw.rectangle([120, 375, 880, 430], fill="#fff0f0", outline="#f5c6cb", width=1)
    draw.text((135, 393), "Invalid text! Please try again.", fill="#c0392b", font=font_bold)

    # Status bar
    draw.text((120, 550), "localhost:5000/emotionDetector?textToAnalyse=", fill="#888", font=get_font(12))

    out_path = os.path.join(os.path.dirname(__file__), "7c_error_handling_interface.png")
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    create_deployment_screenshot()
    create_error_handling_screenshot()
    print("Both screenshots generated successfully.")
