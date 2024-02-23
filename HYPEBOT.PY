# bot.py
import os
import random
import discord
from specificuser import *


#loaddotenv()
token = "-"
GUILD = os.getenv('StopnCop')
TOKEN = os.getenv('-')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!')

@client.event
async def on_message(message):
        if message.author == client.user:
            return

        brooklyn_99_quotes = [
            'Im the human form of the :100: emoji.', 'Bingpot!', 'Cool. Cool cool cool cool cool cool cool, ',
         'no doubt no doubt no doubt no doubt.'
        ]

        if message.content == '99!!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)
        if message.content.startswith('twt'):
            reply = get_tweets(message.content[3:])
            await message.channel.send(reply)

client.run(token)
