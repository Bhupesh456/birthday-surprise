from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Happy Birthday Justine ❤️</title>

    <!-- Confetti Library -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <script>
        window.onload = function() {

            // Confetti effect
            confetti({
                particleCount: 200,
                spread: 100,
                origin: { y: 0.6 }
            });

            alert("🎉💖 Happy 26th Birthday Justine! 🎂✨\\n\\n"
                + "Wish you a very happy birthday my love! 💕\\n\\n"
                + "You are the person I will never forget in my life.\\n\\n"
                + "I always wish for your happiness and success.\\n\\n"
                + "I Love You So Much ❤️");
        }
    </script>
</head>

<body style="text-align:center; background:linear-gradient(to right, #ff9a9e, #fad0c4); padding-top:60px; font-family:Arial;">

    <h1>🎂 Happy 26th Birthday Justine 💕</h1>

    <h2>You are my happiness ❤️</h2>

    <!-- Cake Image -->
    <img src="https://images.unsplash.com/photo-1607478900766-efe13248b125"
         alt="Birthday Cake"
         width="300"
         style="border-radius:20px; box-shadow:0 10px 20px rgba(0,0,0,0.3); margin-top:20px;">

    <p style="margin-top:20px; font-size:18px;">
        From Bhupesh ❤️
    </p>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)