# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

from logging import ERROR
import os

import discord
import asyncio

from commands.activate_clear_message import activate_clear_message
from keep_alive import keep_alive

from commands.hello import hello
from commands.activate_clear_message import activate_clear_message
from commands.random import randomInt
from commands.help import helpMessage
from commands.eightball import eightBall
from commands.send_dm import send_dm
from commands.guessing_number_game import guessing_number_game
from commands.give_role import give_role

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('{0.user} ta online, supostamente.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await hello(message, client)

    if message.content.startswith('.!giverole'):
        await give_role(message, message.content.split()[1], client)

    if message.content.startswith('.!guessnumber'):
        await guessing_number_game(client, message)

    if message.content.startswith('.!dm'):
        _, user_id, *msg_parts = message.content.split()
        msg_content = ' '.join(msg_parts)
        await send_dm(client, message.content.split()[1], msg_content)

    if message.content.startswith('.!8ball'):
        await eightBall(message)

    if message.content == '.!help' or message.content.startswith(
            f'<@{client.user}>'):
        await helpMessage(message)

    if message.content.startswith('.!clear'):
        await activate_clear_message(message, message.author)

    if message.content.startswith('.!random'):
        await randomInt(message)


keep_alive()
try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
