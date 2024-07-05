from discord.utils import get

async def give_role(message, role, client):
    member = message.content.split()[2]
    await client.add_roles(member, role)