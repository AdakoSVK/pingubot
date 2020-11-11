# bot.py

import martins_funcs as m

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

m.chyba()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if '99' in message.content:
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

@client.event
async def on_message(message):
    answer = m.f_martin(message,client)
    if answer != False:
    	await message.channel.send(answer)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
