# bot.py

import martins_funcs as m
import adams_functions as adam


import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

m.chyba()

@client.event
async def on_message(message):
    answer = m.f_martin(message,client)
    if answer != False:
    	await message.channel.send(answer)
    else:
        answer = adam.f_adam(message,client)
        if answer != False:
            await message.channel.send(answer)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
