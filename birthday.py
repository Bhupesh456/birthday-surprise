from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Happy Birthday Justine ❤️</title>
    <script>
        window.onload = function() {
            alert("🎉👩‍🦰💖 Happy 26th Birthday Justine! 💖🎂✨\\n\\n"
            + "Wish you a very happy birthday, my love! ❤️\\n\\n"
            + "You are the person I will never forget in my life.\\n"
            + "Without you, there is no happiness in my life. 💕\\n\\n"
            + "I always wish for your success and healthy life. 🌸\\n"
            + "Always take care of yourself and keep smiling 😊\\n\\n"
            + "I Love You So Much ❤️🎉");
        }
    </script>
</head>
<body style="text-align:center; background-color:pink; padding-top:100px; font-family:Arial;">
    <h1>🎀 Happy 26th Birthday Justine 🎀</h1>
    <h2>💖 You are my happiness 💖</h2>
    <p>From Bhupesh ❤️</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)