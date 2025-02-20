import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import datetime
import os
from scripts.timeEvents import update_status, send_micheal_message
from scripts.commands import micheal_evangeliet, micheal_github, join_opkald  # Import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN").replace("{", "").replace("}", "")
GUILD_ID = int(os.getenv("GUILD_ID").replace("{", "").replace("}", ""))
CHANNEL_ID = int(os.getenv("CHANNEL_ID").replace("{", "").replace("}", ""))
ROLE_ID = int(os.getenv("ROLE_ID").replace("{", "").replace("}", ""))

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # Enable voice state intents
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    bot.tree.add_command(discord.app_commands.Command(name="micheal_evangeliet", description="Modtag det helligste evangelie i biblen!", callback=micheal_evangeliet))
    bot.tree.add_command(discord.app_commands.Command(name="micheal_github", description="Ændre i micheals syntax", callback=micheal_github))
    await bot.tree.sync() 
    bot.loop.create_task(main_loop())


@bot.event
async def main_loop():
    while not bot.is_closed():
        await send_micheal_message(CHANNEL_ID, ROLE_ID, bot, GUILD_ID)
        await update_status(bot)
        await asyncio.sleep(60)

bot.run(TOKEN)