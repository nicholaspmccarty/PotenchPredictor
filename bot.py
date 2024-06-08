import os
import sys
import subprocess

# Function to install a package
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import nextcord
    from nextcord.ext import commands
except ImportError:
    # If nextcord is not installed, install it.
    install_package("nextcord")
    import nextcord
    from nextcord.ext import commands

import random

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event handler
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(guild_ids=[1119678030026113048], description="Generate a random potential percentage.")
async def whatsthepotench(ctx: nextcord.Interaction, argument: str):
    percentage = random.randint(0, 100)
    await ctx.send(f"The potential for '{argument}' is {percentage}%.")

# Read the token from token.txt file
with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

bot.run(TOKEN)
