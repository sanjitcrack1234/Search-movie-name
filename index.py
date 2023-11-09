import os
from io import BytesIO
import requests
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler, Dispatcher
from movies_scraper import search_movies, get_movie

TOKEN = "Your_Telegram_Bot_Token"
URL = "https://your-vercel-app.vercel.app/"  # Update this with your Vercel app URL
bot = Bot(TOKEN)

app = Flask(__name__)

# ... (rest of the code remains the same)
