import os
import discord

bot = discord.Client(intents=discord.Intents.default())
TOKEN = os.getenv("")

@bot.event
async def on_ready():
    print(f'Ingelogd als {bot.user}')

bot.run(TOKEN)
