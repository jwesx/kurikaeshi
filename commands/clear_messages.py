from discord.ext.commands import has_permissions, CheckFailure


@has_permissions(manage_messages=True)
async def clear_messages(message, amount):
  await message.channel.send(f"Deletando {amount} mensagens...",
                             delete_after=5)

  for i in amount:
    await message.delete()
