import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from flask import Flask, request
import requests

# Your Telegram Bot Token
TOKEN = 'YOUR_BOT_TOKEN'
WEBHOOK_URL = 'YOUR_WEBHOOK_URL'

# Create the bot instance
bot = telegram.Bot(token=TOKEN)

# Create an Updater
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define your command handlers
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your movie search bot. Send me a movie name, and I'll find information about it!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Register command handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Add other handlers for your bot's functionality

# Start your bot
updater.start_polling()

# Create the Flask app
app = Flask(__name)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    url = f'https://api.telegram.org/bot{TOKEN}/setWebhook'
    params = {
        'url': WEBHOOK_URL + '/' + TOKEN
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"

if __name__ == '__main__':
    app.run(debug=True)
