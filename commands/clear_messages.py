async def clear_messages(message, amount):
    if message.content.startswith('.!clear'):
        await message.channel.send(f"Deletando {amount} mensagens...", delete_after=5)

        for i in amount:
            await message.delete()
