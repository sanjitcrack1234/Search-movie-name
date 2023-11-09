from flask import Flask, request
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext

app = Flask(__name__)

# Your Telegram Bot Token
TOKEN = '6525502772:AAFQgq70G7TXJZxZsXFpv6nXMQ5RAu9TK9Q'

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"

@app.route('/{}'.format(TOKEN), methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return ''

if __name__ == '__main__':
    # Start the Flask app
    app.run(port=5000)
