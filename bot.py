import discord
import os
import random

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

# Event handler
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(guild_ids=[1119678030026113048], description="Generate a random potential percentage.")
async def whatsthepotench(ctx, argument: str):
    percentage = random.randint(0, 100)
    await ctx.respond(f"The potential for '{argument}' is {percentage}%.")

# Slash command functionality followed command notation.
@bot.slash_command(description="Shuts down the bot.")
async def shutdown(ctx):
    # Replace YOUR_USER_ID with your actual Discord user ID
    if ctx.author.id == YOUR_USER_ID:
        await ctx.respond("Shutting down...")
        await bot.close()
    else:
        await ctx.respond("You do not have permission to shut down the bot.")
# Next
# Read the token from token.txt file
with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

bot.run(TOKEN)
