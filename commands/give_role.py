import discord

from discord.utils import get
from discord.ext import commands


async def give_role(message, client):
    words = message.content.split()
    guild = message.guild
    member = guild.get_member(int(words[1].replace("<@", "").replace(">", "")))

    role_id = int(words[2].replace("<@&", "").replace(">", ""))
    role = message.guild.get_role(role_id)

    if member is None:
        if role is None:
            await message.channel.send(".!giverole <@user> <@role>")
            return
        await message.author.add_roles(role)

    await member.add_roles(role)
    await message.channel.send(
        f"O cargo '{role.name}' foi adicionado ao {member.display_name}.")
