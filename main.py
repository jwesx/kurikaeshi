# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord
import asyncio

from keep_alive import keep_alive

from commands.hello import hello
from commands.clear_messages import clear_messages

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

    @haspermissions(manage_messages==true)
    if message.content.startswith('.!clear'):
        try:
            await clear_messages(message, int(message.content.split()[1]))
        except:
            await message.channel.send("Quantas? Tem que dizer, fella...",
                                       delete_after=5)
            await asyncio.sleep(0.5)
            await message.channel.send(
                "Ou então tu mandou errado, é .!clear <quantidade> ← em número! 😡",
                delete_after=5)
            await asyncio.sleep(4)
            await message.delete()


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
