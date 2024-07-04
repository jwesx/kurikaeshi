async def clear_messages(message, amount):
  await message.delete()
  await message.channel.purge(limit=amount)
