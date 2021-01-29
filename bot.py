import os

import discord
from discord import member, message
import random


TOKEN = ""
GUILD = "Team VLAD"
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to our Discord server!'
    )


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

    reponse = random.choice(brooklyn_99_quotes)
    await message.channel.send(reponse)
    if 'hi' in message.content.lower():
        await message.channel.send(f'Hi welcome to the non anime disocrd group {message.author}')
    if "nasir" in message.content.lower():
        await message.channel.send(f'yes he is the best programmer {message.author}')
    if "fardeen" in message.content.lower():
        await message.channel.send(f'yes he is the anime watcher {message.author}')
    elif message.content == 'fardeen':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
# print(member, message)
client.run(TOKEN)
