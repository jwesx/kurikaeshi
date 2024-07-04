async def clear_messages(message, amount):
    await message.channel.send(f"Deletando {amount} mensagens...")
