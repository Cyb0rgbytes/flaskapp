from flask import Flask, request, jsonify, render_template
import telegram
import openai

app = Flask(__name__)


# Telegram bot token
TELEGRAM_BOT_TOKEN = "6918262597:AAFw0EXE2-_8BHTTXpyT2VLxp2HK3PzvZ-8"

# OpenAI API key
openai.api_key = "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"

# Initialize Telegram bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        # Get the user's message from the request
        user_message = request.form['ask']

        try:
            # Process the user's message using OpenAI ChatGPT API
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_message,
                max_tokens=100
            )

            # Send the response back to the user via Telegram
            response_text = response['choices'][0]['text']
            # Here you would typically send the message to a specific chat ID or user ID
            # For demonstration purposes, we'll just print the response
            print(response_text)

            return jsonify({"response": response_text})
        except Exception as e:
            return jsonify({"error": str(e)})

    else:
        return render_template("index.html")