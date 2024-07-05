import asyncio

from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

async def clear_messages(message, amount):
  await message.delete()
  await message.channel.purge(limit=amount)


async def activate_clear_message(message, client):
  if message.author.guild_permissions.manage_messages:
    try:
      amount = int(message.content.split()[1])  # Get the amount to clear
      if amount <= 0:
        await message.channel.send("Tem que ser mais que zero, camarada!",
                                   delete_after=5)
      else:
        await clear_messages(message, amount)
        await message.channel.send(
            f"<@{message.author.id}>, {amount} mensagens foram pra vala!",
            delete_after=5)

    except (IndexError, ValueError):
      await message.channel.send("Quantas? Tem que dizer, fella...",
                                 delete_after=5)
      await message.channel.send(
          "Ou então tu mandou errado, é .!clear <quantidade> ← em número! 😡",
          delete_after=5)
      await asyncio.sleep(4)
      await message.delete()
  else:
    await message.channel.send(f"Sem permissão, bobo <@{message.author.id}>.",
                               delete_after=5)
    await asyncio.sleep(5)
    await message.delete()
