async def send_dm(client, user_id, content):
  user_id = int(user_id.replace("<@", "").replace(">", ""))
  user = await client.fetch_user(user_id)

  await user.send(content)
