#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from flask import Flask
from threading import Thread

# --- WEB SERVER SETUP ---
# Ye UptimeRobot ko 24/7 chalaye rakhne ke liye hai.
web = Flask(__name__)

@web.route('/')
def index():
    # Jab UptimeRobot ping karega, toh ye reply milega
    return 'Telegram Bot is Active!'

def run_web():
    # Replit hamesha port 8080 par chalta hai
    web.run(host='0.0.0.0', port=8080) 

t = Thread(target=run_web)
t.start()
# --- WEB SERVER END ---

# --- ORIGINAL BOT CODE START ---
from .bot import Bot

app = Bot()
app.run()
