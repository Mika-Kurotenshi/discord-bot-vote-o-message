import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?!?!', intents=intents)

@bot.event
async def on_ready():
    print("✅ Vote-o-Message connecté et prêt !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == 1327405288977989743 and message.author.id == 318312854816161792:
        print("👀 Message détecté ! Ajout des réactions...")

        emojis = [
            "AleTale:1327407901630926878",
            "FFXIV:1338383446292037713",
            "Minecraft:1327408287804559391",
            "SupermarketTogether:1327409225575698545",
            "Voidtrain:1327407282354524312"
        ]

        for emoji in emojis:
            try:
                await message.add_reaction(emoji)
            except Exception as e:
                print(f"⚠️ Impossible d'ajouter {emoji}: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
