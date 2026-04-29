#Import Required Libraries
import os
import discord
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from core.chips import Economy

#===================================================================================
#RUN BOT
#===================================================================================

#Load token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Set bot intents
intents = discord.Intents.default()
intents.message_content = True

#Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

#Event handlers
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")


#Makes a variable for navigation to commands folder
COMMANDS_DIR = os.path.join(os.path.dirname(__file__), "commands")

bot.economy = Economy()
bot.pending_bets = {}



#===================================================================================
#Message Events
#===================================================================================

@bot.event
async def on_message(message):

    #Prevents interaction with other bots
    if message.author.bot:
        return
    
    await bot.process_commands(message)



#===================================================================================
#Load Command Files
#===================================================================================

async def load_cogs():
    #Iterates through the commands directory and loads all .py command files ignoring __init__.py
    for file in os.listdir(COMMANDS_DIR):
        if file.endswith(".py") and file != "__init__.py":
            await bot.load_extension(f"commands.{file[:-3]}")
            print(f"Loaded {file}")



#===================================================================================
#RUN BOT
#===================================================================================

async def main():
    #Uses async manager to start bot
    async with bot:
        #Waits until the commands are working before starting
        await load_cogs()
        #Connects the code to discord bot
        await bot.start(TOKEN)

#Runs main async function
import asyncio
asyncio.run(main())