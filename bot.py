import os

import discord
import random


TOKEN = "ODAzMjY0OTg3MDE5NDc3MTAy.YA7Q0A.9ukjZnfj1TWMhrYpn_qUY6YR3AM"
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

    if message.content == "99!":
        reponse = random.choice(brooklyn_99_quotes)
        await message.channel.send(reponse)
    if 'hi' in message.content.lower():
        await message.channel.send('Hi how are you?')
    elif message.content == 'fardeen':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
client.run(TOKEN)
