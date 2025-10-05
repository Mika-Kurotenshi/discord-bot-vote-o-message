import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from flask import Flask
import threading

# -----------------------------
# Charger les variables d'environnement
# -----------------------------
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TEST_NOW = os.getenv("TEST_NOW", "false").lower() == "true"

# -----------------------------
# Configuration du bot
# -----------------------------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?!?!', intents=intents)
CHANNEL_ID = 1327405288977989743  # Salon où réagir aux messages
AUTHOR_ID = 318312854816161792    # ID de l'auteur des messages à surveiller

# -----------------------------
# Événements du bot
# -----------------------------
@bot.event
async def on_ready():
    print(f"✅ Vote-o-Message connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and message.author.id == AUTHOR_ID:
        print("Message vu !")
        # Ajouter les réactions
        reactions = [
            "AleTale:1327407901630926878",
            "FFXIV:1338383446292037713",
            "Minecraft:1327408287804559391",
            "SupermarketTogether:1327409225575698545",
            "Voidtrain:1327407282354524312"
        ]
        for r in reactions:
            try:
                await message.add_reaction(r)
            except Exception as e:
                print(f"Erreur réaction {r}: {e}")

# -----------------------------
# Flask pour UptimeRobot
# -----------------------------
app = Flask("")

@app.route("/")
def home():
    return "Vote-o-Message is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask).start()

# -----------------------------
# Lancer le bot
# -----------------------------
bot.run(TOKEN)
