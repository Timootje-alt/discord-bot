import discord
import asyncio
   
TOKEN = "MTM0OTEyMzE2NDQ0NTIxMjk0NQ.GcyEcQ.GBlKp5s8u12KVYVTpqS_O455rlkTYHIxmWfOiI"  # Vervang dit met je echte bot-token
   
intents = discord.Intents.default()
client = discord.Client(intents=intents)
   
@client.event
async def on_ready():
    print(f'Ingelogd als {client.user}')
    activity = discord.Activity(type=discord.ActivityType.watching, name="Westkust Overheid")
    await client.change_presence(status=discord.Status.online, activity=activity)
   
client.run(TOKEN)