async def send_dm(message, client, user_id, content):
  user_id = int(user_id.replace("<@", "").replace(">", ""))
  user = await client.fetch_user(user_id)

  if user == client.user:
    await message.channel.send("Vou mandar uma dm pra mim agora!")

  await user.send(content)
